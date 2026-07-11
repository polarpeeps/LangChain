from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)

"""(.venv) PS C:\Users\nabee\LangChain> & C:\Users\nabee\LangChain\.venv\Scripts\python.exe "c:/Users/nabee/LangChain/5.Structured Outputs/with_structured_output_pydantic.py"
Traceback (most recent call last):
  File "c:\Users\nabee\LangChain\5.Structured Outputs\with_structured_output_pydantic.py", line 1, in <module>
    from langchain_openai import ChatOpenAI
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\langchain_openai\__init__.py", line 4, in <module>
    from langchain_openai.chat_models import AzureChatOpenAI, ChatOpenAI
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\langchain_openai\chat_models\__init__.py", line 3, in <module>
    from langchain_openai.chat_models.azure import AzureChatOpenAI
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\langchain_openai\chat_models\azure.py", line 11, in <module>
    from langchain_core.language_models import LanguageModelInput
  File "<frozen importlib._bootstrap>", line 1423, in _handle_fromlist
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\langchain_core\language_models\__init__.py", line 110, in __getattr__
    result = import_attr(attr_name, module_name, __spec__.parent)
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\langchain_core\_import_utils.py", line 36, in import_attr
    module = import_module(f".{module_name}", package=package)
  File "C:\Users\nabee\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\langchain_core\language_models\base.py", line 42, in <module>
    from transformers import GPT2TokenizerFast  # type: ignore[import-not-found]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1423, in _handle_fromlist
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\transformers\utils\import_utils.py", line 2411, in __getattr__
    fb_module = self._get_module(self._class_to_module[fallback_name])
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\transformers\utils\import_utils.py", line 2537, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\nabee\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\transformers\models\__init__.py", line 510, in <module>
    sys.modules[__name__] = _LazyModule(__name__, _file, define_import_structure(_file), module_spec=__spec__)
                                                         ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^
ure
    import_structure = create_import_structure_from_path(module_path)
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\transformers\utils\import_utils.py", line 2797, in create_import_structure_from_path
    import_structure[entry.name] = create_import_structure_from_path(entry.path)
                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\transformers\utils\import_utils.py", line 2916, in create_import_structure_from_path
    for _all_object in fetch__all__(file_content):
                       ~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Users\nabee\LangChain\.venv\Lib\site-packages\transformers\utils\import_utils.py", line 2702, in fetch__all__
    if line.startswith("__all__"):
       ~~~~~~~~~~~~~~~^^^^^^^^^^^
KeyboardInterrupt
(.venv) PS C:\Users\nabee\LangChain>
                                     & C:\Users\nabee\LangChain\.venv\Scripts\python.exe "c:/Users/nabee/LangChain/5.Structured Outputs/with_structured_output_pydantic.py"
C:\Users\nabee\LangChain\.venv\Lib\site-packages\langchain_openai\chat_models\base.py:2424: UserWarning: Cannot use method='json_schema' with model gpt-3.5-turbo since it doesn't support OpenAI's Structured Output API. You can see supported models here: https://platform.openai.com/docs/guides/structured-outputs#supported-models. To fix this warning, set `method='function_calling'. Overriding to method='function_calling'.
  warnings.warn(
key_themes=['Samsung Galaxy S24 Ultra', 'Snapdragon 8 Gen 3 processor', '5000mAh battery', '45W fast charging', 'S-Pen integration', '200MP camera', 'night mode', 'zoom capabilities', 'weight', 'size', 'Samsung One UI', 'bloatware', 'price'] summary='Nitish Singh praises the Samsung Galaxy S24 Ultra for its powerful Snapdragon 8 Gen 3 processor, long-lasting battery with fast charging, stunning 200MP camera, and useful S-Pen support. However, he notes discomfort in one-handed use due to weight and size, bloatware in Samsung One UI, and the high price tag.' sentiment='pos' pros=['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'] cons=['Weight and size make one-handed use uncomfortable', 'Samsung One UI comes with bloatware', 'High $1,300 price tag'] name='Nitish Singh'"""