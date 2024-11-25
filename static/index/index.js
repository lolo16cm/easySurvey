document.addEventListener("DOMContentLoaded", () => {
    const layoutButton = document.querySelector("#create-blank-form-layout");
    const indexButton = document.querySelector("#create-blank-form-index");
    if (layoutButton) {
        layoutButton.addEventListener("click", () => {
            const csrf = Cookies.get('csrftoken');
            fetch('/create', {
                method: "POST",
                headers: {'X-CSRFToken': csrf},
                body: JSON.stringify({
                    title: "Untitled Form"
                })
            })
            .then(response => response.json())
            .then(result => {
                window.location = `/${result.code}/edit`
            })
        })
    }
    if (indexButton) {
        indexButton.addEventListener("click", () => {
            const csrf = Cookies.get('csrftoken');
            fetch('/create', {
                method: "POST",
                headers: {'X-CSRFToken': csrf},
                body: JSON.stringify({
                    title: "Untitled Form"
                })
            })
            .then(response => response.json())
            .then(result => {
                window.location = `/${result.code}/edit`
            })
        })
    }
})