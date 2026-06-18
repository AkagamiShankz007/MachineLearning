## OCR MODEL HUNT! 

- Sooo....after a little cruise thru the internet i was able to find some ocr models which i could use to build my very own pipeline for museuemscat. 

```
If this is your first time here , then 

A OCR : stands for Optical Character Recognition. 

Which is essentially used to detect n read n extract text from a given uk , image. 

```

| OCR Model  | License | Key Features | Best For | Limits | Final Thoughts|
|----------|----------|----------|----------|----------|---------|
|  PaddleOcr| Apache 2.0 | Multilingual. Handwriting + layout. |Documents , invoices| Requires Tuning.|Shud look into this.|
|Tesseract|Apache 2.0| CPU first , 100+ langs |Bulk printed text , digitization pipelines.|Weak on handwriting and layouts , gpu support|shud look into this|
|Datalab marker | OpenRail | End to End ocr -> Markdown/Json. Optional LLM Processing. | Digitization + RAG , scalable GPT Workload | LLM Mode adds latency. | Shud look into this | 
|Deepseek OCR | MIT |End to end OCR Free transformer | Large Scale GPU OCR and high throughput pipelines | occasional hallucinations + gpu | shud look into this |
| GOT-OCR 2.0| MIT | Visual Language OCR with grounding | mixed visual text docs , scientific papers + slides | High GPU Load and limited layout customization | shud look into this |
| Qwen2.5 - VL | Apache-2.0 \ Qwen License | Multimodal OCR Grounding , high benchmark scores | Complex layout charts , scientific docs | Heavy vram needs license | shud look into this| 
|InternVL 2.5 | MIT | Multimodal Doc understanding 1B-78B | General OCR + Reasoning , PDF Summarization | Large Model Demands , Gpu needs prompt tuning | shud look into this | 
| RolmOCR | Apache 2.0 | Qwen 2.5 VL 7B Fine-tune , low VRAM OCR | Lightweight OCR Deployments | No bounding boxes , limited layout awareness | Shud look into this hmm|






