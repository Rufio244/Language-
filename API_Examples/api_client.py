from Security_Access.access_control import verify_access
from Nexus_Layer.Nexus_1_Main_Langs.ja_es_translate import translate_ja_es

def call_translate(key: str, text: str):
    perm = verify_access(key)
    if perm["ok"]:
        return {"perm":perm,"result":translate_ja_es(text)}
    return perm

if __name__ == "__main__":
    print(call_translate("LCC-244-7A9B-C3D5-E8F0", "こんにちは"))

