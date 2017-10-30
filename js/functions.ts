let remove_words_css: HTMLElement = document.createElement("style"),
    base_css: string = "ruby{padding-left:0.1em;padding-right:0.1em;}";

function generate_css_to_remove_pinyin(word: string){
    return "rt."+word+".phonetic-script{display:none;}ruby."+word+"{padding:0em;}";
}

function run_on_word_click(mouseClick: MouseEvent){
    let clickedWord: string = mouseClick.toElement.classList[0];
    reverse_has_pinyin(clickedWord);
}

function reverse_has_pinyin(word: string){
    let removeCSS: string = generate_css_to_remove_pinyin(word);
    let foundAt: number = remove_words_css.innerHTML.search(removeCSS);
    if (foundAt == -1){
        remove_words_css.innerHTML += removeCSS;
    } else {
        remove_words_css.innerHTML = remove_words_css.innerHTML.replace(removeCSS, "");
    }
}

function add_css_style_for_words(){
    remove_words_css['id'] = "hide_words";
    remove_words_css.innerHTML += base_css;
    document.head.appendChild(
        remove_words_css
    );
}
add_css_style_for_words();
document.addEventListener('click', run_on_word_click);