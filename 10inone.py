# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.Gen.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

#kk = LineAlpha.LINE()
#kk.login(qr=True)
#kk.loginResult()

cl = LineAlpha.LINE() #A
cl.login(token="EonwE6poxC9aZhdFiGt2.WCCRkMNgQXINSOQNF/5yiG.bKw08jfgUahQiuRU3k4HbEDrTffZeZcaNAI4kEyaaZI=")
cl.loginResult()

ki = kk = kc = ks = Lka = Lkb =ko = ke = ku = cl


print "Welcome"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""❧[Auto leave:on/off]
❧[Mid [@TAGORG]]
❧[Set group]
❧[Banned [@]]
❧[Unban [@]]
❧[Kill [@]]
❧[Invite mid]
❧[Spamcontact [@]]
❧[Admin add [@]]]
❧[Albumat']
❧[random: [JUMLAH]]
❧[Admin remove [@]]
❧[Bc [TEKS]]
❧[Group bc [TEKS]]
❧[Contact bc [TEKS]]
✍️T̸̡̛̎ͬͩ̀̂̿́́̾͌̃̋̀́̚͟͜Σ̸̸̲͔̲͖̞̈͑ͦͬ̈ͫ̈́̈́̐̾ͣ́̒Δ̣̰͆͢͡͞M̸̨̧̉́͘͢ ̢̠̮̰̼̈͒̋̊͆̌̐̌ͫ̂ͧ͋ͭͪ̈́͜J̠͂̽̂̏̄͆̌̐̎̾Ω̷̨̨̖̘̹ͬ́́͢͞Ҝ̛̭ͯ͌͒ͭͨ̂̏̔̚͝Σ̯͇̳͕͔ͩͣR̶̬͕̬̟̎ͩ̅͛̽ͤ̇̊ͧ͊͛̚̕͞҉̛̛͘͠͏̵ ̟̮̰̒̒ͣ̀̄̂̔͒̔͋̚͜͝͡β̴̨̛ͫͫ̄͊́̚Ω̫̈ͤ́̋ͩ͂̄̀ͥ͛ͥ̒̈́̇̚Ţ̵̸̸̡̛̲̩̐͛ͦ͌̃̓ͩ̃̏̓ͨ̄̓͆̀̕̕͞͞͠S̳̪̘̒̐̑ͧͦ͏̵̛̀̕͡͡ ✈
"""

Setgroup =""" GROUP PROTECTION

❧[Protect on/off]
❧[Contact on/off]
❧[Cancel on/off]
❧[Join on/off]
"""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
DEF=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = ko.getProfile().mid
Hmid = ke.getProfile().mid
Imid = ku.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,"uc1c72b2a69c6ab18a7b28aa77fee5822","u0d260c353933137641b12142f5027db6","u2e8ed9da95e34448d589355d30d7383e","udc9f0e093b72d43ae4aeb19e3fe00b3b","uaed84a4ed7d8366865c11e5580f78252","u200e9985585fe9a14dfbd61ba4deb895","ufe01bf095486b8926bc4a7a1988c4263","u502f371e0fd162e3af48f6b2e363e65d","u78477fec83b987088e848a0b66b96cf5"]
admin=["uc1c72b2a69c6ab18a7b28aa77fee5822","u481eb86e0cc37a5d060bfea7260a5c43","u0d260c353933137641b12142f5027db6","u2e8ed9da95e34448d589355d30d7383e","udc9f0e093b72d43ae4aeb19e3fe00b3b","uaed84a4ed7d8366865c11e5580f78252","u200e9985585fe9a14dfbd61ba4deb895","ufe01bf095486b8926bc4a7a1988c4263","u502f371e0fd162e3af48f6b2e363e65d","u78477fec83b987088e848a0b66b96cf5"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "UpdateName":True,
    "cName":"",
    "cName2":"ASIST",
    "cName3":"ASIST",
    "cName4":"ASIST",
    "cName5":"ASIST",
    "cName6":"ASIST",
    "cName7":"ASIST",
    "cName8":"ASIST",
    "cName9":"ASIST",
    "cName10":"􀀷􀰂􀰂꧁Kicker꧂􏿿􀀷",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'copy':True,
    'target':{},
    'midsTarget':{},
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in Bots:
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  Ticket = ki.reissueGroupTicket(op.param1)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  ku.kickoutFromGroup(op.param1,[op,param2])
                  ki.updateGroup(G)
                  ku.leaveGroup(op.param1)
        #------Protect Group Kick finish-----#
        #------CCTV-------------===----------#
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 not in admin and Bots:
                   if op.param2 in Bots:
                       pass
                       group = ka.getGroup(op.param1)
                       gMembMids = [contact.mid for contact in group.invitee]
                       random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#

        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)

            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)

            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)

            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)

            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)

            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in admin and Bots:
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  Ticket = ki.reissueGroupTicket(op.param1)
                  ku.acceptGroupInvitationByTicket(op.param1)
                  ku.kickoutFromGroup(op.param1,[op.param2])
                  ki.updateGroup(G)
                  ku.leaveGroup(op.param1)
        #---------------------------------#

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ks.updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True        
                    
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak Ada")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif "Sangein " in msg.text:
              if msg.from_ in admin:
                sangein0 = msg.text.replace("Sangein ","")
                sangein1 = sangein0.rstrip()
                sangein2 = sangein1.replace("@","")
                sangein3 = sangein2.rstrip()
                _name = sangein3
                gs = ki.getGroup(msg.to)
                ginfo = ki.getGroup(msg.to)
                gs.preventJoinByTicket = False
                ki.updateGroup(gs)
                invsend = 0
                Ticket = ki.reissueGroupTicket(msg.to)
                ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        ku.kickoutFromGroup(msg.to,[target])
                                        ku.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        ku.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        ki.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        ki.updateGroup(gs)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Set group"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "_second kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "_third kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "_fourth kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "sinvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "tinvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "finvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak ada")
                        else:
                            cl.sendText(msg.to,"Sukses")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","ourl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","curl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link Close")
                    else:
                        cl.sendText(msg.to,"Already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id Group" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,msg.to)
            elif "Mid LL" == msg.text:
              if msg.from_ in admin:
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
                ko.sendText(msg.to,Gmid)
                ke.sendText(msg.to,Hmid)
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Join on","join on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","join off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect on","protect on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect off","protect off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Set View"]:
                md = ""
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+=" Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+=" Block Group Off\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+=" Cancel All Invited Off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["B gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["C gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["D gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #--------------------------------------------------------#            
         #--------------------------------------------------------#

         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Y"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ke.sendText(msg.to,"Sudah lengkap")
                        G = ke.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ke.updateGroup(G)
                        print "All complete"
                        G.preventJoinByTicket(G)
                        ke.updateGroup(G)

            elif msg.text in ["A join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["C join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["D join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["O"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        cl.sendText(msg.to,"Sudah keluar")
                    except:
                        pass
            elif msg.text in ["A leave"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Out"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ku.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye D"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv1 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv2 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv3 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#

    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Summon"]:
              if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Cleanse" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Cleanse 」\nSlow aja relax")
                    ki.sendText(msg.to,"「 Cleanse 」\nMwa")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[ki,kk,kc,ks,ka]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Slow sih")
                                kk.sendText(msg.to,"Gausa ditangkis")
                                kc.sendText(msg.to,"Biasain aja")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Hai " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Hai ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Aw")
                                    kc.sendText(msg.to,"Hehehe")
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                ki.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
#-----------------------------------------------
            elif "Kedapkedip " in msg.text.lower():
                  txt = msg.text.replace("Kedapkedip ", "")
                  t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                  t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                  cl.sendText(msg.to, t1 + txt + t2)
#-----------------------------------------------
#----------------Commandtambahan----------------------#
            elif msg.text in ["List group","Glist"]:
              if msg.from_ in admin:
               gid = cl.getGroupIdsJoined()
               h = ""
               for i in gid:
                h += "[⭐] %s  \n" % (cl.getGroup(i).name + " | Members : " + str(len (cl.getGroup(i).members)))
               cl.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))
               
            elif msg.text in ["Creator"]:
                if msg.toType == 2:
                      msg.contentType = 13
                      Creatorbot = "uc1c72b2a69c6ab18a7b28aa77fee5822"
                      try:
                          msg.contentMetadata = {'mid': Creatorbot}
                        
                      except:
                        Creatorbot = "Error"
                      cl.sendText(msg.to, "🅂🅄🄿🄿🄾🅁🅃 🄱🅈 🄹🄾🄺🄴🅁 🄱🄾🅃 🄰🄽🄳 🄳🄹")
                      cl.sendMessage(msg)
                      
            elif "Admin add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Admin remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Adminlist","adminlist"]:
                if admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

            elif "Spam " in msg.text:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   if txt[1] == "on":
                        if jmlh <= 50:
                             for x in range(jmlh):
                               cl.sendText(msg.to,teks)
                   elif txt[1] == "off":
                         if jmlh <= 100:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")

            elif "Group bc " in msg.text:
               bctxt = msg.text.replace("Group bc ", "")
               n = cl.getGroupIdsJoined()
               for manusia in n:
                  cl.sendText(manusia, (bctxt))
                  
            elif "Contact bc " in msg.text:
               bctxt = msg.text.replace("Contact bc ", "")
               t = cl.getAllContactIds()
               for manusia in t:
                  cl.sendText(manusia, (bctxt))
                  
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
                                        
#------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                   print "[Command]dp executing"
                   _name = msg.text.replace("Steal dp @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except:
                               pass
                   print "[Command]dp executed"
#-----------------------------------------------------------
                               
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)
                        
            elif "copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.cloneContactProfile(target)
                               cl.sendText(msg.to, "Suksesclone...")
                            except Exception as e:
                                print e
                                
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to, "Suksesbackup...")
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
#------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                   print "[Command]dp executing"
                   _name = msg.text.replace("Steal dp @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except:
                               pass
                   print "[Command]dp executed"
#-----------------------------------------------------------
            elif msg.text in ["Reboot"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"Rebooting")
                    exit(1)
                    
            elif "Restart" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
                    
            elif "Allrespon: " in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Allrespon: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                if len(string.ecode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                    
            elif msg.text in ["Set"]:
                 if msg.toType == 2:
                    cl.sendText(msg.to, "Check")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "set point"
                    
            elif msg.text == "Lurking":
                if msg.toType == 2:
                    cl.sendText(msg.to, "Set reading point:" + datetime.datetime.today().strftime('\n%Y-%m-%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "Result":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\n [?]?Powered By: NevadaBot" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.datetime.today().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")
#-----------------------------------------------
            
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#

        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Spam"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
                cl.sendText(msg.to,"Feri ganteng")
                ki.sendText(msg.to,"Feri ganteng")
                kk.sendText(msg.to,"Feri ganteng")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt))
				ka.sendText(msg.to,(bctxt))
				kb.sendText(msg.to,(bctxt))
				ko.sendText(msg.to,(bctxt))
				ke.sendText(msg.to,(bctxt))
				ku.sendText(msg.to,(bctxt))
				
       #--------------Fungsi Broadcast Finish-----------#


            elif msg.text in ["Welcome"]:
                ki.sendText(msg.to,"Selamat datang ")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
#-------------------------------------------------------
            elif 'XpertCrash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc1c72b2a69c6ab18a7b28aa77fee5822,'"}
                cl.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
                cl.sendMessage(msg)
#-------------------------------------------------------
#-------------------------------------------------------
            elif 'Crash' in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uc1c72b2a69c6ab18a7b28aa77fee5822,'"}
                cl.sendMessage(msg)
#-------------------------------------------------------  
            elif msg.text in ["404"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.404.")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"HADIR BOS")
                kk.sendText(msg.to,"HADIR BOS")
                kc.sendText(msg.to,"HADIR BOS")
                ks.sendText(msg.to,"HADIR BOS")
                ka.sendText(msg.to,"HADIR BOS")
                kb.sendText(msg.to,"HADIR BOS")
                ko.sendText(msg.to,"HADIR BOS")
                ke.sendText(msg.to,"HADIR BOS")
      #-------------Fungsi Respon Finish---------------------#

      #-------------Fungsi Balesan Respon Start---------------------#
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa jadi")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
                
            elif msg.text in ["Quote","quote","quotes","Quotes"]:
                quote = ['Aku sayang kamu']
                psn = random.choice(quote)
                cl.sendText(msg.to,psn)

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","speedbot","speed","sp","Sp"]:
              if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "Collecting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#
#------------------------------------------------------#
            elif msg.text in ["UpdateName"]:
              if msg.from_ in admin:
               if wait["UpdateName"] == True:
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile = ki.getProfile()
                profile.displayName = wait["cName2"]
                kk.updateProfile(profile)

                profile = kk.getProfile()
                profile.displayName = wait["cName3"]
                kk.updateProfile(profile)

                profile = kc.getProfile()
                profile.displayName = wait["cName4"]
                kc.updateProfile(profile)


                profile = ks.getProfile()
                profile.displayName = wait["cName5"]
                ks.updateProfile(profile)


                profile = ka.getProfile()
                profile.displayName = wait["cName6"]
                ka.updateProfile(profile)


                profile = kb.getProfile()
                profile.displayName = wait["cName7"]
                kb.updateProfile(profile)


                profile = ko.getProfile()
                profile.displayName = wait["cName8"]
                ko.updateProfile(profile)


                profile = ke.getProfile()
                profile.displayName = wait["cName9"]
                ke.updateProfile(profile)


                profile = ku.getProfile()
                profile.displayName = wait["cName10"]
                ku.updateProfile(profile)
  #--------------------------------------------------------#
      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ks.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"di usir")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・" + Name
                        wait2['ROM'][op.param1][op.param2] = "・" + Name
                else:
                    cl.sendText
            except:
                pass


        if op.type == 59:
            print op


    except Exception as error:
        print error
        
def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["UpdateName"] == True:
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
