css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.techrepublic.com/wp-content/uploads/2023/07/tr71123-ai-art.jpeg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/C5103AQHT_Npi_-FgGg/profile-displayphoto-shrink_800_800/0/1516425631625?e=1703721600&v=beta&t=fkC2Q0RCiTLCufuH7XvWDGKZl_FF5kquXvNZjVcWAtw">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''