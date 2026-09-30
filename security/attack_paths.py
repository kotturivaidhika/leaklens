def get_attack_paths(data):
    classes={str(x).lower() for b in data.get("breaches",[]) for x in b.get("data_classes",[])}
    rules=[
      (("password",),"Credential stuffing","Attackers may try exposed or reused passwords on other services."),
      (("email",),"Targeted phishing","Scammers may send convincing fake login or security messages."),
      (("phone",),"Phone-based social engineering","Scammers may attempt impersonation or request OTPs."),
      (("address",),"Identity/account-recovery abuse","Address details may make impersonation attempts seem credible."),
      (("date of birth","government","identity"),"Identity impersonation","Identity details can be combined with other information.")]
    out=[{"title":t,"description":d} for keys,t,d in rules if any(k in c for k in keys for c in classes)]
    return out or [{"title":"Stay alert","description":"Use unique passwords and MFA; no specific attack path was inferred."}]
