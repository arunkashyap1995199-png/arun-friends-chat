from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ArunFriendsChat(App):
    def build(self):
        self.ignored_users = [] 
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.header = Label(
            text="[ ARUN FRIENDS CHAT ]", 
            font_size='24sp', 
            size_hint_y=0.1,
            color=(0, 1, 0, 1)
        )
        self.main_layout.add_widget(self.header)

        self.scroll = ScrollView(size_hint_y=0.6)
        self.chat_logs = Label(text="[सिस्टम]: अरुण का 10th क्लास सिस्टम चालू है!\n", valign='top', size_hint_y=None, text_size=(400, None))
        self.scroll.add_widget(self.chat_logs)
        self.main_layout.add_widget(self.scroll)

        self.privacy_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=5)
        self.hide_input = TextInput(hint_text="किसका मैसेज छुपाना है? नाम डाल...", multiline=False)
        self.hide_btn = Button(text="छुपाओ", size_hint_x=0.3, background_color=(1, 0, 0, 1))
        self.hide_btn.bind(on_press=self.hide_user)
        self.privacy_layout.add_widget(self.hide_input)
        self.privacy_layout.add_widget(self.hide_btn)
        self.main_layout.add_widget(self.privacy_layout)

        self.input_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=5)
        self.user_input = TextInput(hint_text="तेरा नाम", size_hint_x=0.3)
        self.msg_input = TextInput(hint_text="मैसेज लिखो...", multiline=False)
        self.send_btn = Button(text="Send", size_hint_x=0.2, background_color=(0, 0.6, 0, 1))
        self.send_btn.bind(on_press=self.send_message)
        
        self.input_layout.add_widget(self.user_input)
        self.input_layout.add_widget(self.msg_input)
        self.input_layout.add_widget(self.send_btn)
        self.main_layout.add_widget(self.input_layout)
        
        return self.main_layout

    def send_message(self, instance):
        sender = self.user_input.text if self.user_input.text else "अंजन"
        txt = self.msg_input.text
        if txt:
            if sender in self.ignored_users:
                self.msg_input.text = ""
                return
            self.chat_logs.text += f"{sender}: {txt}\n"
            self.msg_input.text = ""

    def hide_user(self, instance):
        user_to_hide = self.hide_input.text
        if user_to_hide and user_to_hide not in self.ignored_users:
            self.ignored_users.append(user_to_hide)
            self.chat_logs.text += f"\n[प्राइवेसी]: अब से {user_to_hide} के मैसेज तुझे नहीं दिखेंगे!\n"
            self.hide_input.text = ""

if __name__ == "__main__":
    ArunFriendsChat().run()
  
    
      
