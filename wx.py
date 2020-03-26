# import itchat, time
# def lc():
#     print("Finash Login!")
# def ec():
#     print("exit")
#
# itchat.auto_login(loginCallback=lc, exitCallback=ec)
# time.sleep()
# itchat.logout()    #强制退出登录

# import itchat
# #
# # itchat.auto_login(enableCmdQR=2, hotReload=True)
# #
# # groups = ['测试这是', '测试2']
# #
# # mediaId = None
# # for i in groups:
# #     res, media_id = itchat.search_chatrooms(name=i)[0].send_video('a.mp4', mediaId=mediaId)
# #     mediaId = media_id

# import itchat

# from itchat.content import TEXT


# @itchat.msg_register
# def simple_reply(msg):
#     if msg['Type'] == TEXT:
#         return 'I received: %s' % msg['Content']
#
#
# itchat.auto_login()
#
# itchat.run()

import itchat

# 登录
itchat.login()
# 发送消息
itchat.send(u'你好', 'filehelper')