# Türkçe Cümleler için Morfolojik Analiz Modeli

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/obenadak/turkce-morfolojik-analiz)
[![Model Card](https://img.shields.io/badge/%F0%9F%A4%97%20Model-turkce--morfolojik--analiz-blue)](https://huggingface.co/obenadak/turkce-morfolojik-analiz-mt0-small)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Bu proje, Türkçe bir cümlenin derinlemesine morfolojik analizini yapabilen bir sequence-to-sequence modeli içerir. Model, [Hugging Face Transformers](https://github.com/huggingface/transformers) kütüphanesi kullanılarak `bigscience/mt0-small` modelinin `universal_dependencies` (`tr_boun` alt kümesi) veri seti üzerinde ince ayarlanmasıyla (fine-tuning) eğitilmiştir.

Proje, modelin eğitim kodlarını, değerlendirme metriklerini ve interaktif bir web demosunu içerir.

> ### **[İnteraktif Demo](https://huggingface.co/spaces/obenadak/turkce-morfolojik-analiz)**
![Gradio Arayüzü Demosu](screenshots\image.png)

## Projenin Amacı

Model, kendisine verilen bir Türkçe cümledeki her bir kelimeyi alarak aşağıdaki yapısal bilgilere ayrıştırır:
- **Kök (Lemma):** Kelimenin anlam taşıyan en temel hali.
- **Kelime Türü (Part-of-Speech):** Kelimenin cümledeki görevi (isim, fiil, sıfat vb.).
- **Ekler (Affixes):** Kelimenin aldığı çekim ve yapım ekleri (çoğul, iyelik, zaman ekleri vb.).

**Örnek Çıktı:**
```
Girdi: Kitapları masanın üstüne koydum.

Çıktı:
Kitapları -> kitap(isim) + -ler(çoğul) + -i(belirtme)
masanın -> masa(isim) + (tekil) + -in(tamlayan)
üstüne -> üst(isim) + (3.kişi iyelik) + (iyelik tekil) + -e(yönelme)
koydum -> koy(fiil) + -di(geçmiş z.) + (1.kişi) + (belirli geçmiş) + (olumlu)
. -> .(noktalama)
```

## Kurulum ve Kullanım

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### Gereksinimler
- Python 3.8+
- Git

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/obenadak/turkce-morfolojik-analiz.git
cd turkce-morfolojik-analiz
```

### 2. Gerekli Kütüphaneleri Yükleyin

Proje bağımlılıklarını `requirements.txt` dosyasından yükleyin.

```bash
pip install -r requirements.txt
```

### 3. Modeli Python İçinde Kullanma

Modeli `transformers` kütüphanesinin `pipeline` özelliği ile kolayca kullanabilirsiniz.

```python
from transformers import pipeline

# Modeli Hugging Face Hub'dan yükle
model_repo = "obenadak/turkce-morfolojik-analiz-mt0-small"
analiz_cihazi = pipeline("text2text-generation", model=model_repo)

# Analiz edilecek cümle
cumle = "Gelecek hafta sonu için planların neler?"

# Analizi gerçekleştir
sonuc = analiz_cihazi(cumle, max_length=512)

print(sonuc[0]['generated_text'])
```
