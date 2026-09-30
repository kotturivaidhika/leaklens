def calculate_risk(data):
    breaches=data.get("breaches",[])
    classes={str(x).lower() for b in breaches for x in b.get("data_classes",[])}
    if not breaches: return 0,"LOW",["No matching breaches were returned."]
    score=min(25,max(0,(len(breaches)-1)*10))
    reasons=[f"{len(breaches)} known breach record(s) found."]
    rules=[
      (("password",),25,"Password-related data appears exposed."),
      (("phone",),15,"Phone number information appears exposed."),
      (("address",),10,"Address information appears exposed."),
      (("credit card","financial","bank account"),30,"Financial information appears exposed."),
      (("date of birth","government","identity","social security"),20,"Identity-related information appears exposed."),
      (("email",),5,"Email address information appears exposed.")]
    for keys,points,reason in rules:
        if any(k in c for k in keys for c in classes):
            score+=points; reasons.append(reason)
    score=min(score,100)
    level="LOW" if score<=25 else "MODERATE" if score<=50 else "HIGH" if score<=75 else "CRITICAL"
    reasons.insert(0,"Illustrative heuristic only; not a probability of being attacked.")
    return score,level,reasons
