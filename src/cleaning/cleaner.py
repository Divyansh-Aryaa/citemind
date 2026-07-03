
# This is responsible for cleaning the data after INGESTION and then send it further down the pipline for RETRIEVAL and PREDICTION


from langchain_core.documents import Document


from src.cleaning.utils import(
    normalize_unicode,
    repair_hyphenation,
    collapse_spaces,
    collapse_blank_lines,
    remove_trailing_spaces   
)


def clean_documents(documents: list[Document]) -> list[Document]:

    cleaned_documents = [] #list of the cleaned documents we will get from cleaning the original documents

    for doc in documents:

        text = doc.page_content ## page content is the actual text content of the document

        #Rule 0 Normalize unicode characters 
        text = normalize_unicode(text)

        #Rule 0.5 Repare hyphenated words
        text = repair_hyphenation(text)

        #Rule 1 Using strip() to remove leading and trailing whitespace characters from the text.
        text = text.strip()

        #Rule 2 Using regex to replace multiple consecutive spaces or tabs with a single space.
        text = collapse_spaces(text)

        #Rule 3 Using regex to replace three or more consecutive newline characters with two newline characters. 
             #This helps to reduce excessive blank lines in the text.
        text = collapse_blank_lines(text)

        #Rule 4 Using splitlines() to split the text into individual lines, 
        # then using rstrip() to remove trailing whitespace from each line, and finally joining the cleaned lines back together with newline characters.
        text = remove_trailing_spaces(text)
        
        cleaned_doc = Document(
            page_content = text,

            metadata = doc.metadata.copy()
        )

        cleaned_documents.append(cleaned_doc)

    return cleaned_documents 


if __name__ == "__main__":

    from pathlib import Path
    from src.ingestion.loader import load_documents

    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    DATA_DIR = PROJECT_ROOT / "data" / "raw"

    docs, stats = load_documents(DATA_DIR)

    cleaned_docs = clean_documents(docs)

    total_original = 0
    total_cleaned = 0

    for original, cleaned in zip(docs, cleaned_docs):
        total_original += len(original.page_content)
        total_cleaned += len(cleaned.page_content)

    characters_removed = total_original - total_cleaned
    reduction = (characters_removed / total_original) * 100

    print("=" * 60)
    print("CLEANING SUMMARY")
    print("=" * 60)

    print(f"Documents Processed : {len(docs)}")
    print(f"Original Characters : {total_original:,}")
    print(f"Cleaned Characters  : {total_cleaned:,}")
    print(f"Characters Removed : {characters_removed:,}")
    print(f"Reduction Percentage : {reduction:.2f}%")
    print("\nCleaning completed successfully.\n")
    



    ## DEBUG CODE ##  

    # print("=" * 60)
    # print("CLEANING SUMMARY FOR 1 DOCUMENT")
    # print("=" * 60)

    # print(f"Original Length : {len(docs[0].page_content)}")
    # print(f"Cleaned Length : {len(cleaned_docs[0].page_content)}")
    # print(f"Characters Removed : {len(docs[0].page_content) - len(cleaned_docs[0].page_content)}")

   
