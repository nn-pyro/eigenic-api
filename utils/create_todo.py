from utils import llm
from utils.process_data import process_content
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain_core.prompts import PromptTemplate

def create_todolist(content_meting: str):

    chunks = process_content(content_meting)

    prompt_template = """
        Đây là bản ghi âm cuộc họp: {text}.
        Hãy tạo một danh sách công việc (to-do list) từ nội dung cuộc họp dựa trên thông tin có trong bản ghi. Danh sách cần rõ ràng và chi tiết, đảm bảo các nhiệm vụ và hành động cụ thể được liệt kê một cách chính xác.
        Mỗi mục trong danh sách cần bao gồm:
        Nhiệm vụ: Mô tả ngắn gọn về công việc cần thực hiện.
        Vui lòng sử dụng suy luận hợp lý để xác định những nhiệm vụ có thể bị thiếu hoặc không rõ ràng trong bản ghi. Danh sách công việc cần tối thiểu 10 mục để đảm bảo độ chi tiết và đầy đủ.
    """
    prompt = PromptTemplate.from_template(prompt_template)
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
    todo_list_content = stuff_chain.run(chunks)

    return todo_list_content