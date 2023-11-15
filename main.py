import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    TextSendMessage,
    ImageSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageAction,
)

def linebot(request):
    try:
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        line_bot_api = LineBotApi('Ki9QCY0RHAbiZHh77Z9Fhk9FAUC0Vot7Qp0xj3LsU0seubuk/zh7Sq3tdDtyh9wGpggvshK2XR21Syu6Pq5htTxNSuLdZHwjn0Ltg0ZFMLBLH76qYEzj2y8d/H5nuRrSe/odVTr3O4boxUzfLvrOegdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('b84c6bc475c1044fc8e86ed4efd07019')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        tp = json_data['events'][0]['message']['type']
        if tp == 'text':
            msg = reply_msg(json_data['events'][0]['message']['text'])
            if msg[0] == 'text':
                line_bot_api.reply_message(tk, TextSendMessage(text=msg[1]))
            if msg[0] == 'image':
                line_bot_api.reply_message(tk, ImageSendMessage(original_content_url=msg[1], preview_image_url=msg[1]))
            if msg[1].lower() == '#法律諮詢':
                buttons_template_message = buttons_template_law()
                line_bot_api.reply_message(tk, buttons_template_message)
            if msg[1].lower() == '#合約':
                buttons_template_message = buttons_template_contract()
                line_bot_api.reply_message(tk, buttons_template_message)
        if tp == 'image':
            line_bot_api.reply_message(tk, TextSendMessage(text='恭喜您上傳了合約！'))
    except Exception as e:
        print('error', str(e))
    return 'OK'

def reply_msg(text):
    msg_dict = {
        '#收款': '開發中，敬請期待',
        '#租客管理': '開發中，敬請期待',
    }
    img_dict = {
    }
    
    text_lower = text.lower()  # 統一轉換為小寫以進行比對
    if text_lower in msg_dict:
        reply_msg_content = ['text', msg_dict[text_lower]]
    elif text_lower in img_dict:
        reply_msg_content = ['image', img_dict[text_lower]]
    return reply_msg_content

def buttons_template_law():
    buttons_template_message = TemplateSendMessage(
        alt_text='法律諮詢',
        template=ButtonsTemplate(
            title='法律諮詢',
            text='以下為您提供相關服務：',
            actions=[
                MessageAction(
                    label='常見問題',
                    text='查看常見問題'
                ),
                MessageAction(
                    label='租屋懶人包',
                    text='我要租屋懶人包'
                ),
                MessageAction(
                    label='諮詢專區',
                    text='我要諮詢'
                )
            ]
        )
    )
    return buttons_template_message

def buttons_template_contract():
    buttons_template_message = TemplateSendMessage(
        alt_text='合約相關',
        template=ButtonsTemplate(
            title='合約',
            text='提供以下合約相關服務：',
            actions=[
                URIAction(
                    label='合約範本',
                    uri='https://s30.aconvert.com/convert/p3r68-cdx67/avby5-bep73.html'
                ),
                MessageAction(
                    label='上傳合約',
                    uri='https://lurl.cc/img.html'
                ),
                URIAction(
                    label='查看合約',
                    text='尚未開發'
                )
            ]
        )
    )
    return buttons_template_message

