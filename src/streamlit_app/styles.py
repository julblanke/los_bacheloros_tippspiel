main_style = """
<style>
/* 1. Banner Container */
.banner {
    width: 100%;
    height: 240px;
    background: url('https://i.pinimg.com/736x/14/78/d3/1478d36f359a69604b9acec196e95730.jpg') center/cover no-repeat;
    position: relative;
    border-radius: 0 0 1rem 1rem;
    margin: 0;
}

/* 3. Global App Background */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(
        circle at bottom right,
        #8b0000 0%,
        #ffe4e1 50%,
        #ffffff 100%
    );
    padding-top: 0;
    font-family: 'Playfair Display', Georgia, serif;
    color: #222;
}

/* 4. Tabs */
[data-baseweb="tab"] {
    background-color: #ffe9eb;
    color: #5b1220;
    padding: 0.4rem 1rem;
    border-radius: 0.5rem 0.5rem 0 0;
    font-weight: 700;
    font-family: 'Playfair Display', serif;
    margin-right: 0.5rem;
    transition: background-color 0.2s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}
[data-baseweb="tab"][aria-selected="true"] {
    background-color: #5b1220;
    color: #fff;
    box-shadow: inset 0 -3px 0 #ffa3b1;
}

/* 5. Buttons */
.stButton>button {
    background-color: #c2185b;
    color: #fff;
    border-radius: 0.5rem;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
    font-family: 'Playfair Display', serif;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    transition: background-color 0.2s ease, transform 0.1s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.stButton>button:hover {
    background-color: #880e4f;
    transform: translateY(-1px);
}
.stButton>button:active {
    transform: translateY(0);
}

/* 6. Tables & Markdown */
.stTable, .stMarkdown {
    border-radius: 0.75rem;
    padding: 1.5rem;
    background: rgba(255,255,255,0.95);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    line-height: 1.8;
    font-family: 'Georgia', serif;
    color: #333;
}

/* 7. Headings */
h1, h2, h3, h4 {
    color: #3e001f;
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    margin-bottom: 0.75rem;
    letter-spacing: 1px;
}

/* 8. Bar labels */
.bar-label {
    background: #fff;
    padding: 0.3rem 0.6rem;
    border-radius: 0.3rem;
    color: #000 !important;
    font-weight: 700;
    font-family: 'Georgia', serif;
    font-size: 1.1rem !important;
}

/* Style right-side score numbers */
.right-number {
    background: #fff;
    padding: 0.3rem 0.6rem;
    border-radius: 0.3rem;
    color: #000 !important;
    font-weight: 700;
    font-family: 'Georgia', serif;
    font-size: 2rem !important;
}

/* Ensure any table-cell numbers are black and larger */
.stTable td,
.stTable th {
    color: #000 !important;
    font-size: 1.2rem !important;
}

/* Hide default Streamlit header & menu */
header, [data-testid="stToolbar"], #MainMenu, .css-18e3th9 {
    display: none !important;
}
/* Remove top padding around main content */
.block-container {
    padding-top: 0 !important;
}
</style>
"""
