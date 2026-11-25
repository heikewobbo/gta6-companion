import re
def anchors(chapters, mission_chs, db):
    """item -> (slug, 'before'|'during'|'after'|'merge'|'any')"""
    out = {}
    for c in chapters:
        mc = next((x for x in mission_chs if x["n"] == c["n"]), None)
        if not mc: continue
        names = {}
        for x in mc["m"]:
            m = db[x["id"]]
            for nm in {m.get("it"), re.split(r" \(| – ", m["n"])[0]}:
                if nm and len(nm) >= 5: names[nm] = x["id"]
        rx = re.compile("(" + "|".join(re.escape(n) for n in sorted(names, key=len, reverse=True)) + ")")
        def find(s):
            m = rx.search(s or ""); return (names[m.group(1)], m) if m else (None, None)
        for i in c["items"]:
            if i.get("mis"): out[i["id"]] = (i["mis"], "merge"); continue
            t, d = i["t"], i.get("d", "")
            sid, m = find(t)
            if sid:
                pre = t[:m.start()].lower()
                out[i["id"]] = (sid, "before" if pre.rstrip(" «").endswith("prima di") else "during"); continue
            sid, m = find(d)
            if sid:
                pre = d[:m.start()].lower().rstrip(" «")
                if pre.endswith("prima di") or pre.endswith("prima che inizi") or pre.endswith("spariscono dopo") or pre.endswith("chiude dopo"): pos = "before"
                elif pre.endswith("dopo") or pre.endswith("si apre dopo"): pos = "after"
                elif pre.endswith("inizio di") or pre.endswith("durante") or pre.endswith("in"): pos = "during"
                else: pos = "any"
                out[i["id"]] = (sid if pos != "any" else None, pos); continue
            out[i["id"]] = (None, "any")
    return out
