var btnAddToCarts = document.getElementsByClassName("add-to-cart");
for(i=0; i<btnAddToCarts.length; i++) {
    btnAddToCarts[i].addEventListener("click", function(){
        var itemId = this.dataset.itemId
        console.log("itemId:", itemId);
        addToCart(itemId)
    })
} 

function addToCart(itemId){
    console.log("itemId:", itemId);
    var url = "/cart/add_to_cart/"
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            "itemId": itemId
        })
    })
    .then((response)=>{
        if (response.status != 200 || (response.url && response.url.includes('/login/'))) {
            window.location.href = "/login/";
        }
        return response.json()
    })
    .then((data)=>{
        console.log("total items", data.total)
        // location.reload()
        document.getElementById('cart').innerText= data.total
    })
    .catch((error)=>{
        console.log("error", error)
    })
}
