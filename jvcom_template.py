import streamlit as st
import requests
import datetime
st.set_page_config(layout="wide")


header = '''
<link href="https://static.jvc.gg/22.24.2/css/skin-common.css" rel="stylesheet" />
<link href="https://static.jvc.gg/22.24.2/css/skin-forum.css" rel="stylesheet" />
'''
head = '''
<header class="header js-header" data-gtm-vis-first-on-screen-1087040_133="168" data-gtm-vis-total-visible-time-1087040_133="1000" data-gtm-vis-has-fired-1087040_133="1">
    <div class="header__top">
        <div class="header__container">
            <div class="bloc_header">
                <img src="https://info.lewagon.com/hubfs/Logo_Red%26White-3.png" height='50' class="user-avatar-msg js-lazy avatar">
            </div>
            <div class="header__globalUser">
                <button type="button" class="header__navLinkSearch js-header-nav-search">
                    <i class="icon-search"></i>
                </button>
                <div class="headerAccount headerAccount--connect">
                        <span class="headerAccount__img"><i class="icon-account"></i></span>
                    </a>
                </div>
                <button type="button" class="toggleTheme" onclick="window.jvc.toggleTheme();"></button>
            </div>
        </div>
    </div>
    <div class="headerSearch" data-label="Recherche">
        <span class="headerSearch__close icon-close js-header-nav-search-close"></span>
</header>
'''

message_body = '''
<br>
<br>
<br>
<br>
<div class="bloc-message-forum mx-2 mx-lg-0 " data-id="1211163144">
<div class="conteneur-message">
    <div class="bloc-header">
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-avatar-msg"
        target="_blank">
        <img src="https://www.pngmart.com/files/22/User-Avatar-Profile-Download-PNG-Isolated-Image.png" width='50' height='50' class="user-avatar-msg js-lazy avatar">
    </span>
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-pseudo-msg text-user"
        target="_blank">
        Stephanie
    </span>
    <div class="bloc-options-msg"></div>
    <div class="bloc-date-msg">
        <span class="JvCare 1F444FC1C34EC21F4E43C2C24A4C431F2A212A2A2A24222A2B2B lien-jv" target="_blank">05/12/2022 11:36:57</span>
    </div>
    </div>
    <div class="bloc-contenu">
    <div class="txt-msg  text-enrichi-forum ">
        <p>Salut tout le monde</p>
        <p>Est-ce que quelqu'un saurait comment charger un fichier CSS externe avec streamlit ?</p>
        <p>J'ai cherché sur Stack Overflow mais je n'ai pas trouvé la réponse</p>
    </div>
    </div>
</div>
</div>
'''

message_body2 = '''
<div class="bloc-message-forum mx-2 mx-lg-0 " data-id="1211163144">
<div class="conteneur-message">
    <div class="bloc-header">
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-avatar-msg"
        target="_blank">
        <img src="https://www.pngmart.com/files/22/User-Avatar-Profile-Download-PNG-Isolated-Image.png" width='50' height='50' class="user-avatar-msg js-lazy avatar">
    </span>
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-pseudo-msg text-user"
        target="_blank">
        Eloi
    </span>
    <div class="bloc-options-msg"></div>
    <div class="bloc-date-msg">
        <span class="JvCare 1F444FC1C34EC21F4E43C2C24A4C431F2A212A2A2A24222A2B2B lien-jv">06/12/2022 14:50:24</span>
    </div>
    </div>
    <div class="bloc-contenu">
    <div class="txt-msg  text-enrichi-forum ">
        <p>Salut Stéphanie</p>
        <p>J'ai trouvé une solution sur ce lien, ça peut peut-être t'aider. https://discuss.streamlit.io/t/css-hacks/14501</p>
    </div>
    </div>
</div>
</div>
'''
msg_list = [header,head,message_body,message_body2]

st.components.v1.html(''.join(msg_list),height=500)
with st.sidebar:
    with st.form("message"):
        st.write("Bonjour Demo_Day_User, que souhaitez-vous répondre ?")
        username = "Demo_Day_User"
        entre = st.text_area("Votre message :")
        submitted = st.form_submit_button("Répondre")



if submitted:

    url = 'https://jvcom-t4wrmxgprq-ew.a.run.app/pred'
    params = {
    'text': f"{entre}"
    }

    type = requests.get(url, params=params).json()['type']

    if type == 0:
        msg =f'''
<div class="bloc-message-forum mx-2 mx-lg-0 " data-id="1211163144">
<div class="conteneur-message">
    <div class="bloc-header">
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-avatar-msg"
        target="_blank">
        <img src="https://www.pngmart.com/files/22/User-Avatar-Profile-Download-PNG-Isolated-Image.png" width='50' height='50' class="user-avatar-msg js-lazy avatar">
    </span>
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-pseudo-msg text-user"
        target="_blank">
        {username}
    </span>
    <div class="bloc-options-msg"></div>
    <div class="bloc-date-msg">
        <span class="JvCare 1F444FC1C34EC21F4E43C2C24A4C431F2A212A2A2A24222A2B2B lien-jv">{str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))}</span>
    </div>
    </div>
    <div class="bloc-contenu">
    <div class="txt-msg  text-enrichi-forum ">
        <p>{entre}</p>
    </div>
    </div>
</div>
</div>
'''
        st.components.v1.html(''.join([header,msg]),height=300)
    else:
        msg=f'''
<div class="bloc-message-forum mx-2 mx-lg-0 " data-id="1211163144">
<div class="conteneur-message">
    <div class="bloc-header">
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-avatar-msg"
        target="_blank">
        <img src="https://www.pngmart.com/files/22/User-Avatar-Profile-Download-PNG-Isolated-Image.png" width='50' height='50' class="user-avatar-msg js-lazy avatar">
    </span>
    <span
        class="JvCare 45CBCBC0C22D1F1FCCCCCC194D43C3C5C4464B434F19424F4E1FC0C14F4446481FC04649473F44484A4E46494C4F2F4E4F4B432E4649444FC2 bloc-pseudo-msg text-user"
        target="_blank">
        <I>Nom d'utilisateur masqué</I>
    </span>
    <div class="bloc-options-msg"></div>
    <div class="bloc-date-msg">
        <span class="JvCare 1F444FC1C34EC21F4E43C2C24A4C431F2A212A2A2A24222A2B2B lien-jv">{str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))}</span>
    </div>
    </div>
    <div class="bloc-contenu">
    <div class="txt-msg  text-enrichi-forum ">
        <p>🚨<I> Le contenu de ce message a été supprimé car il ne respecte pas la charte d'utilisation de ce forum. </I>🚨</p>
    </div>
    </div>
</div>
</div>
'''
        st.components.v1.html(''.join([header,msg]),height=300)
