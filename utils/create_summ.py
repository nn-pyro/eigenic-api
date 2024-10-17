from utils import llm
from utils.process_data import process_content
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain_core.prompts import PromptTemplate

def create_summary(content_meting: str):

    chunks = process_content(content_meting)

    prompt_template = """
        Đây là bản ghi âm cuộc họp: {text}. 
        Hãy tóm tắt nội dung đầy đủ của cuộc họp dựa trên thông tin có trong bản ghi, không thêm bớt hoặc bịa ra những nội dung không có.\
        Bản tóm tắt cần trình bày rõ ràng, rành mạch, đảm bảo các ý chính được diễn đạt một cách chính xác và chi tiết.\
        Độ dài tối thiểu của bản tóm tắt là 500 từ để đảm bảo mức độ chi tiết và chính xác.\
        Vì công nghệ chuyển giọng nói thành văn bản có thể gặp lỗi, hãy sử dụng suy luận hợp lý và chính xác khi xác định những nội dung có thể bị thiếu hoặc không rõ ràng.\
        Không sử dụng ngôi thứ trong phần tóm tắt.
    """
    prompt = PromptTemplate.from_template(prompt_template)
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
    summary_content = stuff_chain.run(chunks)

    return summary_content