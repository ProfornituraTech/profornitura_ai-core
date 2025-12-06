"""AI CHATBOT GATEWAY – Stub (Blueprint)

Non integra realmente un LLM.
Definisce solo il formato di una futura API tra ERPNext e un chatbot esterno.

Funzioni previste:
- ricevere una domanda con contesto (es. gara, entità)
- inoltrarla a un motore AI
- salvare domanda/risposta su ERPNext (AI Chat Session / AI Chat Message)

In questa versione:
- stampa a schermo una risposta finta
- non chiama nulla di esterno.
"""


def main():
    print("\n==============================================")
    print(" PROFORNITURA AI – CHATBOT GATEWAY (STUB)")
    print("==============================================\n")    

    question = input("Domanda (demo): ").strip()
    print("\n[DEMO AI RESPONSE]")
    print("Hai chiesto:", question)
    print("Risposta simulata: questa è una risposta di esempio generata dal gateway stub.\n")


if __name__ == "__main__":
    main()
