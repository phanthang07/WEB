from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').lower().strip()

        # Danh sách từ khóa và phản hồi tương ứng
        responses = {
            "chào": "Chào bạn! Tôi là trợ lý ảo của bạn.",
            "hi": "Chào bạn! Tôi là trợ lý ảo của bạn.",
            "xin chào": "Xin chào! Tôi có thể giúp gì cho bạn hôm nay?",
            "giờ làm": "Chúng tôi làm việc từ 8h đến 18h từ thứ Hai đến thứ Bảy.",
            "bạn là ai": "Tôi là chatbot hỗ trợ tự động, sẵn sàng hỗ trợ bạn mọi lúc.",
            "số điện thoại": "Bạn có thể gọi đến số 0903 166 696 để được hỗ trợ.",
            "cảm ơn": "Không có gì, rất vui được giúp bạn!",
            "cảm ơn bạn": "Bạn luôn được chào đón!",
            "thông tin liên hệ": "Bạn có thể gọi đến số 0903 166 696 hoặc đến trực tiếp văn phòng chúng tôi.",
            "liên hệ": "Bạn có thể liên hệ qua số điện thoại 0903 166 696 hoặc đến địa chỉ văn phòng.",
            "địa chỉ": "Số 10, Đường D2, Khu tái định cư Chánh Nghĩa, Phường Chánh Nghĩa, Thành phố Thủ Dầu Một, Tỉnh Bình Dương.",
            "tôi cần hỗ trợ": "Bạn cần hỗ trợ vấn đề gì? Vui lòng cho tôi biết rõ hơn nhé.",
            "có ai không": "Tôi luôn ở đây để hỗ trợ bạn!",
            "bạn làm được gì": "Tôi có thể cung cấp thông tin liên hệ, giờ làm việc và trả lời một số câu hỏi thường gặp.",
            "giá dịch vụ": "Bạn vui lòng cho biết loại dịch vụ bạn quan tâm, tôi sẽ cung cấp thông tin cụ thể hơn.",
            "dịch vụ": "Chúng tôi cung cấp nhiều dịch vụ khác nhau. Bạn vui lòng cung cấp thêm chi tiết bạn muốn biết về dịch vụ nào?",
            "hẹn gặp": "Bạn muốn đặt lịch hẹn? Vui lòng cung cấp thời gian và tên để chúng tôi hỗ trợ bạn.",
            "làm việc ngày lễ không": "Chúng tôi không làm việc vào các ngày lễ theo quy định của nhà nước.",
            "thanh toán": "Chúng tôi hỗ trợ thanh toán qua chuyển khoản, tiền mặt hoặc ví điện tử.",
        }

        # Tìm từ khóa nào nằm trong user_message
        reply = "Xin lỗi, tôi chưa hiểu câu hỏi của bạn."
        for keyword, response in responses.items():
            if keyword in user_message:
                reply = response
                break

        return JsonResponse({'reply': reply})

    return JsonResponse({'reply': 'Vui lòng gửi POST request.'})
