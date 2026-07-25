# -*- coding: utf-8 -*-
"""🔒 Access Control — 35 keys total"""

VALID_KEYS = [
    "LCC-244-7A9B-C3D5-E8F0",
    "LCC-244-1F2G-H4J6-K9L1",
    "LCC-244-3M4N-P5Q7-R2S4",
    "LCC-244-5T6U-V8W2-X3Y5",
    "LCC-244-7Z8A-B2C4-D6E8",
    "LCC-244-9F1G-H3J5-K7L9",
    "LCC-244-2M3N-P4Q6-R8S1",
    "LCC-244-4T5U-V7W9-X1Y3",
    "LCC-244-6Z7A-B1C3-D5E7",
    "LCC-244-8F9G-H2J4-K6L8",
    "LCC-244-1M2N-P3Q5-R7S9",
    "LCC-244-3T4U-V5W7-X9Y2",
    "LCC-244-5Z6A-B7C9-D1E3",
    "LCC-244-7F8G-H9J1-K3L5",
    "LCC-244-9M1N-P2Q4-R6S8",
    "LCC-244-2T3U-V4W6-X8Y1",
    "LCC-244-4Z5A-B6C8-D9E2",
    "LCC-244-6F7G-H8J9-K1L3",
    "LCC-244-8M9N-P1Q2-R4S6",
    "LCC-244-1T2U-V3W5-X7Y9",
    "LCC-244-3Z4A-B5C7-D8E1",
    "LCC-244-5F6G-H7J9-K2L4",
    "LCC-244-7M8N-P9Q1-R3S5",
    "LCC-244-9T1U-V2W4-X6Y8",
    "LCC-244-2Z3A-B4C6-D7E9",
    "LCC-244-4F5G-H6J8-K9L2",
    "LCC-244-6M7N-P8Q1-R2S4",
    "LCC-244-8T9U-V1W3-X5Y7",
    "LCC-244-1Z2A-B3C5-D6E8",
    "LCC-244-3F4G-H5J7-K8L1",
    "LCC-244-5M6N-P7Q9-R1S3",
    "LCC-244-7T8U-V9W2-X4Y6",
    "LCC-244-9Z1A-B2C4-D5E7",
    "LCC-244-2F3G-H4J6-K7L9",
    "LCC-244-4M5N-P6Q8-R9S2"
]

def verify_access(key: str):
    if key.startswith("GENAI-") or key.startswith("IP-"):
        return {"ok":True,"level":"CREATIVE_FREE"}
    if key in VALID_KEYS:
        return {"ok":True,"level":"FULL_CORE"}
    return {"ok":False,"reason":"Owner permission required"}

if __name__ == "__main__":
    print(verify_access("GENAI-TEST"))
    print(verify_access("LCC-244-7A9B-C3D5-E8F0"))

