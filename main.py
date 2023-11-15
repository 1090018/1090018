import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    TextSendMessage,
    ImageSendMessage,
    ConfirmTemplate,
    MessageAction,
    TemplateSendMessage,
    CarouselTemplate,
    CarouselColumn,
    PostbackAction,
    URIAction,
)

def linebot(request):
    try:
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        line_bot_api = LineBotApi('sHu2YBno6O21jcXhCnWJzHc1lIiLsdmEuBCPbns5wl9IOrtpTMl718p+iGZ1Uk8KSdRs778JmBaW5N11eU8bQNvQ92P2IhBJS26VyvmA8jRtICO02sBE3kZkPp27AiwQQF5m0EhrLZ8l6fGwl0fRUQdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('4e55f1e294a38074c4c783c721391649')
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
            if msg[0] == 'template':
                buttons_template_message = buttons_template()
                line_bot_api.reply_message(tk, buttons_template_message)
            if msg[0] == 'carousel':
                carousel_template_message = carousel_template()
                line_bot_api.reply_message(tk, carousel_template_message)
            if msg[0] == 'Contract':
                Contract_template_message = Contract_template()
                line_bot_api.reply_message(tk, Contract_template_message)
        if tp == 'image':
            line_bot_api.reply_message(tk, TextSendMessage(text='好圖給讚！'))
    except:
        print('error', body)
    return 'OK'

def reply_msg(text):
    msg_dict = {
        '#收款': '開發中，敬請期待',
        '#租客管理': '開發中，敬請期待',
    }
    img_dict = {
        '#合約': 'https://www.houseol.com.tw/Upload/Knowledge/2/K000000150_S_0.jpg',
    }
    
    if text in msg_dict:
        reply_msg_content = ['text', msg_dict[text.lower()]]
    elif text in img_dict:
        reply_msg_content = ['image', img_dict[text.lower()]]
    elif text == '#選項':
        reply_msg_content = ['template']  # 回傳模板消息
    elif text == '法律諮詢':
        reply_msg_content = ['carousel']  # 回傳 Carousel 消息
    elif text == '合約專區':
        reply_msg_content = ['Contract']  # 回傳 Contract 消息
    
    return reply_msg_content

def buttons_template():
    buttons_template_message = TemplateSendMessage(
        alt_text='Carousel Button template',
        template=ConfirmTemplate(
            text='以下為您提供相關服務：',
            actions=[
                MessageAction(
                    label='查詢合約',
                    text='查詢合約'
                ),
                MessageAction(
                    label='上傳合約',
                    text='上傳合約'
                )
            ]
        )
    )
    return buttons_template_message

def carousel_template():
    carousel_template_message = TemplateSendMessage(
        alt_text='CarouselTemplate',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='法律諮詢',
                    text='以下為您提供相關服務：',
                    actions=[
                        MessageAction(
                            label='常見問題',
                            text='常見問題一覽'
                        ),
                        MessageAction(
                            label='租屋懶人包',
                            text='我要租屋懶人包'
                        ),
                        MessageAction(
                            label='諮詢專區',
                            text='諮詢專區'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template_message


def Contract_template():
    Contract_template_message = TemplateSendMessage(
        alt_text='ContractTemplate',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='合約專區',
                    text='以下為您提供相關服務：',
                    actions=[
                        MessageAction(
                            label='查詢合約',
                            text='查詢合約'
                        ),
                        MessageAction(
                            label='上傳合約',
                            text='上傳合約'
                        ),
                    ]
                )
            ]
        )
    )
    return Contract_template_message
