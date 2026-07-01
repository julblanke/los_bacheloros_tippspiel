from typing import List, Dict

IMG_KATALINA = "https://www.rtl.de/img/30717395/1776267338/o/1200/1200/katalina11529.webp"
IMG_JOSI = "https://www.rtl.de/img/30717391/1776267545/o/1200/1200/josi4b1c5.webp"
IMG_NADJA = "https://www.rtl.de/img/30717384/1776267127/o/1200/1200/nadja7ab76-1.webp"
IMG_PAULINA = "https://www.rtl.de/img/30717398/1776267097/o/1200/1200/paulnaabd27.webp"
IMG_KIM = "https://www.rtl.de/img/30717381/1776267074/o/1200/1200/kimjulia93932-1.webp"
IMG_VIVIEN = "https://www.rtl.de/img/30717400/1776265326/o/1200/1200/vivibc59c-1.webp"
IMG_JANETTE = "https://www.rtl.de/img/30717387/1776267465/o/1200/1200/janettec67ce.webp"
IMG_MICHELLE = "https://www.rtl.de/img/30717390/1776267433/o/1200/1200/michelle31577.webp"
IMG_YANA = "https://www.rtl.de/img/30717379/1776267150/o/1200/1200/yana73715.webp"
IMG_NATALIE = "https://www.rtl.de/img/30717383/1776267213/o/1200/1200/natalie7d0ff.webp"
IMG_LAURA = "https://www.rtl.de/img/30717393/1776267318/o/1200/1200/laura7b097.webp"
IMG_KATARINA = "https://www.rtl.de/img/30717389/1776267524/o/1200/1200/katarinac9a7f.webp"
IMG_JULIANA = "https://www.rtl.de/img/30717386/1776267289/o/1200/1200/juleac5ef.webp"
IMG_PLACEHOLDER = "https://i.pinimg.com/736x/d3/4e/c5/d34ec52e51bef130bb5f881daed91a8d.jpg"
IMG_LIA = "https://www.rtl.de/img/30717404/1776267364/o/1200/1200/liae0383.webp"
IMG_CHIARA = "https://www.rtl.de/img/30717396/1776267500/o/1200/1200/chiara6172b.webp"
IMG_SEBASTIAN = "https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.instagram.com%2Fitssebastianpaul%2F&ved=0CBYQjRxqFwoTCKCrrum665QDFQAAAAAdAAAAABAF&opi=89978449"
IMG_TIM = "https://www.google.com/imgres?q=bachelor%20tim%20%202026&imgurl=https%3A%2F%2Fi0.web.de%2Fimage%2F910%2F42051910%2Cpd%3D1%2Cf%3Dsize-l%2Ftim-reitz.jpg&imgrefurl=https%3A%2F%2Fweb.de%2Fmagazine%2Funterhaltung%2Fthema%2Ftim-reitz&docid=TwHQ9Nsy5w6iyM&tbnid=DsqhNb7x7uf-6M&vet=12ahUKEwjXv_30uuuUAxUjgf0HHRIpCvMQnPAOegQIKhAB..i&w=543&h=680&hcb=2&ved=2ahUKEwjXv_30uuuUAxUjgf0HHRIpCvMQnPAOegQIKhAB"

TEAM_IMAGES: Dict[str, List[str]] = {
    "Anja":     [IMG_KATALINA, IMG_JOSI, IMG_NADJA, IMG_PAULINA, IMG_KIM, IMG_VIVIEN, IMG_SEBASTIAN],
    "Josefine": [IMG_NADJA, IMG_JANETTE, IMG_MICHELLE, IMG_YANA, IMG_KATALINA, IMG_VIVIEN, IMG_SEBASTIAN],
    "Marie":    [IMG_NATALIE, IMG_VIVIEN, IMG_NADJA, IMG_LAURA, IMG_YANA, IMG_KATALINA, IMG_TIM],
    "Julian":   [IMG_NADJA, IMG_JANETTE, IMG_LAURA, IMG_KATALINA, IMG_LIA, IMG_JOSI, IMG_TIM],
    "Mert":     [IMG_LIA, IMG_KATALINA, IMG_YANA, IMG_VIVIEN, IMG_KIM, IMG_PAULINA, IMG_TIM],
    "Luisa":    [IMG_PLACEHOLDER, IMG_PLACEHOLDER, IMG_PLACEHOLDER, IMG_PLACEHOLDER, IMG_PLACEHOLDER, IMG_PLACEHOLDER],
    "Anne":     [IMG_CHIARA, IMG_LIA, IMG_KATARINA, IMG_VIVIEN, IMG_YANA, IMG_NADJA, IMG_SEBASTIAN],
}

IMAGE_NAME_MAP: Dict[str, str] = {
    IMG_KATALINA: "Katalina",
    IMG_JOSI: "Josi",
    IMG_NADJA: "Nadja",
    IMG_PAULINA: "Paulina",
    IMG_KIM: "Kim",
    IMG_VIVIEN: "Vivien",
    IMG_JANETTE: "Janette",
    IMG_MICHELLE: "Michelle",
    IMG_YANA: "Yana",
    IMG_NATALIE: "Natalie",
    IMG_LAURA: "Laura",
    IMG_KATARINA: "Katarina",
    IMG_JULIANA: "Julia",
    IMG_LIA: "Lia",
    IMG_CHIARA: "Chiara",
    IMG_SEBASTIAN: "Sebastian",
    IMG_TIM: "Tim",
    IMG_PLACEHOLDER: "TBA",
}


def get_team_images(person: str) -> List[str]:
    images = TEAM_IMAGES.get(person, [])
    if len(images) < 7:
        images += [IMG_PLACEHOLDER] * (6 - len(images))
    return images
