from typing import List, Dict


IMG_LENA = "https://www.rtl.de/img/4370049/1747732080/c16_9/1024/bachelor-kandidatin-lena.webp"
IMG_CLARA = "https://www.rtl.de/img/4370043/1747743223/c16_9/1024/bachelor-kandidatin-clara.webp"
IMG_SEYMA = "https://www.rtl.de/img/4370071/1747732936/c16_9/1024/bachelor-kandidatin-seyma.webp"
IMG_AYLIN = "https://www.rtl.de/img/4370182/1747743206/c16_9/1024/bachelor-kandidatin-aylin.webp"
IMG_PAULINA = "https://www.rtl.de/img/4370502/1747821770/c16_9/1024/49747-2jpg.webp"
IMG_VIVIANE = "https://www.rtl.de/img/4370080/1747821560/c16_9/1024/1c958-3jpg.webp"
IMG_ANN_KATHRIN = "https://www.rtl.de/img/4370030/1747731438/c16_9/1024/bachelor-kandidatin-ann-kathrin.webp"
IMG_LEONIE = "https://www.rtl.de/img/4370053/1747732222/c16_9/1024/bachelorkandidatin-leonie.webp"
IMG_LOUISA = "https://www.rtl.de/img/4370552/1747743628/c16_9/1024/louisa.webp"
IMG_NADINE = "https://www.rtl.de/img/4370494/1747821737/c16_9/1024/87137-2jpg.webp"
IMG_ISABELLE = "https://www.rtl.de/img/4370471/1747741941/c16_9/1024/bachelor-kandidatin-isabelle.webp"
IMG_HANNAH = "https://www.rtl.de/img/4370542/1747743408/c16_9/1024/bachelor-kandidatin-hannah.webp"
IMG_PLACEHOLDER = "https://i.pinimg.com/736x/55/a5/b3/55a5b3f247eba55ee4a1ccb8acc27035.jpg"


TEAM_IMAGES: Dict[str, List[str]] = {
    "Valentin": [IMG_LENA, IMG_CLARA, IMG_SEYMA, IMG_AYLIN, IMG_PAULINA, IMG_VIVIANE],
    "Julian":   [IMG_ANN_KATHRIN, IMG_VIVIANE, IMG_PAULINA, IMG_CLARA, IMG_LEONIE, IMG_LOUISA],
    "Anja":     [IMG_LENA, IMG_CLARA, IMG_SEYMA, IMG_NADINE, IMG_AYLIN, IMG_ISABELLE],
    "Josy":     [IMG_SEYMA, IMG_LENA, IMG_AYLIN, IMG_VIVIANE, IMG_ISABELLE, IMG_NADINE],
    "Luisa":    [IMG_ISABELLE, IMG_CLARA, IMG_VIVIANE, IMG_AYLIN, IMG_NADINE, IMG_LEONIE],
    "Marie":    [IMG_LENA, IMG_SEYMA, IMG_VIVIANE, IMG_NADINE, IMG_PAULINA, IMG_CLARA],
    "Mert":     [IMG_ANN_KATHRIN, IMG_AYLIN, IMG_HANNAH, IMG_LENA, IMG_NADINE, IMG_SEYMA],
    "Rabea":    [IMG_PLACEHOLDER] * 6,
}


IMAGE_NAME_MAP: Dict[str, str] = {
    IMG_LENA: "Lena",
    IMG_CLARA: "Clara",
    IMG_SEYMA: "Seyma",
    IMG_AYLIN: "Aylin",
    IMG_PAULINA: "Paulina",
    IMG_VIVIANE: "Viviane",
    IMG_ANN_KATHRIN: "Ann-Kathrin",
    IMG_LEONIE: "Leonie",
    IMG_LOUISA: "Louisa",
    IMG_NADINE: "Nadine",
    IMG_ISABELLE: "Isabelle",
    IMG_HANNAH: "Hannah",
    IMG_PLACEHOLDER: "TBA",
}


def get_team_images(person: str) -> List[str]:
    images = TEAM_IMAGES.get(person, [])
    if len(images) < 6:
        images += [IMG_PLACEHOLDER] * (6 - len(images))
    return images
