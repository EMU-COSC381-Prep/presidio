from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

engine = AnonymizerEngine()
result = engine.anonymize(
    text="My name is Jason, Jason Cava",
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=11, end=16, score=0.8),
        RecognizerResult(entity_type="PERSON", start=18, end=28, score=0.8),
    ],
    operators={"PERSON": OperatorConfig("replace", {"new_value": "jcava17"})},
)
try:
    print(result.text, end="")
except AttributeError:
    print(result["text"], end="")
