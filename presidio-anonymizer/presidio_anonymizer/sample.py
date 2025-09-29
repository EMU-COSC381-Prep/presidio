from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int, new_value: str = "BIP"):
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": new_value})},
    )

    out_text = result.text if hasattr(result, "text") else result["text"]
    out_items = result.items if hasattr(result, "items") else result["items"]

    print(f"text: {out_text}")
    print("items:")
    print(out_items)

    return result  # return so it can be tested

if __name__ == "__main__":
    sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")
