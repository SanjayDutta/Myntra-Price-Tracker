from win10toast import ToastNotifier


class PCN:
    def __init__(self,header,message):
        hr =ToastNotifier()
        hr.show_toast(header,message)