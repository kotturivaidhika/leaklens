def get_recommendations(data):
    classes={str(x).lower() for b in data.get("breaches",[]) for x in b.get("data_classes",[])}
    tips=[]
    if any("password" in c for c in classes):
        tips += ["Change exposed passwords anywhere they are still used.","Use unique passwords and consider a password manager.","Enable MFA, especially for email and banking."]
    if any("phone" in c for c in classes):
        tips += ["Never share OTPs with callers or message senders.","Contact your mobile provider through its official channel if SIM-swap activity is suspected."]
    if any("email" in c for c in classes):
        tips += ["Check sender addresses, domains, and links before clicking.","Visit important services through their official website or app."]
    if any(any(k in c for k in ("address","date of birth","identity","government")) for c in classes):
        tips += ["Be alert for impersonation attempts using personal details.","Verify requests before sharing more identity information."]
    if not tips: tips=["Use unique passwords and enable MFA on important accounts.","Be cautious of unexpected requests for personal information."]
    return list(dict.fromkeys(tips))
