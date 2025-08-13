import gradio as gr
from transformers import pipeline
import textwrap


hf_kullanici_adi = "obenadak" 
hf_model_adi = "turkce-morfolojik-analiz-mt0-small" 
model_repo_id = f"{hf_kullanici_adi}/{hf_model_adi}"

try:
    analiz_cihazi = pipeline("text2text-generation", model=model_repo_id)
    print(f"'{model_repo_id}' modeli başarıyla yüklendi.")
except Exception as e:
    print(f"Model yüklenirken hata oluştu: {e}")
    analiz_cihazi = None

def morfolojik_analiz_et(cumle):
    if analiz_cihazi is None:
        return "Model yüklenemediği için analiz yapılamıyor. Lütfen Space loglarını kontrol edin."
    
    if not cumle or not cumle.strip():
        return "Lütfen analiz etmek için bir cümle girin."
        
    try:
        sonuc = analiz_cihazi(cumle, max_length=512)[0]['generated_text']
        
        analizler = [a.strip() for a in sonuc.split('|')]
        okunakli_sonuc = "\n".join(analizler)
        
        return okunakli_sonuc
    except Exception as e:
        return f"Analiz sırasında bir hata oluştu: {e}"

title = "Türkçe Morfolojik Analiz Modeli"
description = textwrap.dedent("""
    Bu arayüz, **[turkce-morfolojik-analiz-mt0-small](https://huggingface.co/obenadak/turkce-morfolojik-analiz-mt0-small)** modelini kullanarak bir Türkçe cümlenin morfolojik analizini yapar. 
    Aşağıdaki kutuya bir cümle yazın ve "Analiz Et" düğmesine tıklayın. Model, cümlenizdeki her kelimenin kökünü, türünü ve eklerini ayrıştıracaktır.
""")
article = "Oben Adak tarafından geliştirilmiştir. [Model Sayfası](https://huggingface.co/obenadak/turkce-morfolojik-analiz-mt0-small) | [GitHub Reposu](https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ)" # GitHub linkini güncelleyin

demo = gr.Interface(
    fn=morfolojik_analiz_et,
    inputs=gr.Textbox(lines=3, label="Analiz Edilecek Cümle", placeholder="Örn: Kitap okumayı çok seviyorum."),
    outputs=gr.Textbox(label="Morfolojik Analiz Sonucu", lines=10),
    title=title,
    description=description,
    article=article,
    examples=[
        ["Çok güneşli bir günde yapılacak en iyi şey evde kalmaktır."],
        ["Gelecek hafta sonu için planların neler?"],
        ["Evden çıkarken ışıkları kapatmayı unutmuşum."],
    ]
)

# Arayüzü başlat
if __name__ == "__main__":
    demo.launch()