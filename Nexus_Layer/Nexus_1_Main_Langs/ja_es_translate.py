# -*- coding: utf-8 -*-
"""Nexus(1): JA → ES via hidden EN"""

CORE_MAP = {
    "JA": {"word":"こんにちは","mean":"การทักทาย","pron":"konnichiwa"},
    "EN": {"word":"Hello","mean":"General greeting","pron":"həˈləʊ"},
    "ES": {"word":"Hola","mean":"Saludo general","pron":"ˈo.la"}
}

def translate_ja_es(text: str) -> dict:
    if text == CORE_MAP["JA"]["word"]:
        return {
            "source": CORE_MAP["JA"],
            "via": "EN (hidden)",
            "result": CORE_MAP["ES"]
        }
    return {"error":"Not found"}

if __name__ == "__main__":
    import json
    print(json.dumps(translate_ja_es("こんにちは"), indent=2, ensure_ascii=False))

