from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

text = "My name is Jason, Jason Cava."

engine = AnonymizerEngine()
result = engine.anonymize(
<<<<<<< Updated upstream
    text=text,
=======
    text="My name is Jason, Jason Cava.",
>>>>>>> Stashed changes
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=11, end=16, score=0.8),
        RecognizerResult(entity_type="PERSON", start=18, end=28, score=0.8),
    ],
    operators={"PERSON": OperatorConfig("replace", {"new_value": "jcava17"})},
)
<<<<<<< Updated upstream

try:
    print(result.text)
except AttributeError:
    print(result["text"])
=======
print(result.text if hasattr(result, "text") else result["text"])
>>>>>>> Stashed changes
