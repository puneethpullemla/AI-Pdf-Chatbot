from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langchain_core.language_models.llms import LLM
from typing import Optional, List, ClassVar, Any


class FlanT5LLM(LLM):

    model_name: ClassVar[str] = "google/flan-t5-base"

    tokenizer: Any = None
    model: Any = None

    def __init__(self):
        super().__init__()

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200
        )

        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return answer

    @property
    def _llm_type(self) -> str:
        return "flan_t5"


def get_llm():
    return FlanT5LLM()