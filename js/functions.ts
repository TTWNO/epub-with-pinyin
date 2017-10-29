let remove_words_css: HTMLElement = document.createElement("style");

function run_on_word_click(e: HTMLElement){
    let clickedWord: String = e.classList[0];
    console.log(clickedWord);
}

function remove_pinyin_css(word: string){
    remove_words_css.innerHTML += "."+word+".phonetic-script{visibility:hidden;}";
}

function add_css_style_for_words(){
    remove_words_css['id'] = "hide_words";
    document.head.appendChild(
        remove_words_css
    );
}
add_css_style_for_words();