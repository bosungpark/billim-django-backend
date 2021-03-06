from django.shortcuts import render, redirect, get_object_or_404
from book.models import MajorBook
from book.forms import BorrowedBookForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

def rental(request, id):
    """
    책 빌리기 기능 함수
    """
    rental_book = MajorBook.objects.get(pk=id)
    rental_status=rental_book.status
    
    if rental_status == '대여 가능':
        user=UserChangeForm(instance = request.user).save(commit=False)
        if user.coin:
            if user.coin>0:
                if rental_book.uploader != user:
                    user.coin-=1
                    user.save()

                    rental_book.status = '대여중'
                    rental_book.save()

                    #등록한 책이 대여 되었을 때, 업로더의 코인 +2 해줍니다.
                    uploader=UserChangeForm(instance = rental_book.uploader).save(commit=False)
                    uploader.coin+=2
                    uploader.save()

                    messages.success(request, '대여가 성공했습니다!')

                    form=BorrowedBookForm().save(commit=False)
                    form.borrower=request.user
                    form.borrow_book=rental_book
                    form.save()
                else:
                      messages.success(request, '자신이 등록한 책은 대여하실 수 없습니다!')     
        else:
            messages.success(request, '코인이 부족합니다!')
        return redirect('book_list')