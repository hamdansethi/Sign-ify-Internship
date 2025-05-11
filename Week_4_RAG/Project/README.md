## WEEKLY PROJECT
Build on your RAG implementation from day 1 which involved answering questions based on a
file, and extend it to include document-lifecycle functionality, as follows:
- Your application will take an input path with multiple files, both .pdf and .docx.
- The pipeline should create embeddings on the vector store.
- In case new documents are added (or some documents are removed), the pipeline should
update the embeddings accordingly in the vector store.
- Similarly, if an individual document changes, the embeddings should change as well