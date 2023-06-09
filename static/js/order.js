let inputs = document.querySelectorAll(".quantity");

let grand_total = document.querySelector("#grant_total")
let total_prices = document.querySelectorAll(".total_price")


function updateGrantTotal() {
    let total = 0
    total_prices.forEach((total_price) => {
        total += parseFloat(total_price.innerHTML)
    })
    grand_total.innerHTML = total
    }

inputs.forEach((input) => {
    input.addEventListener('change', (event) => {
        let total_price = event.target.value * parseFloat(event.target.dataset.price)
        document.querySelector(`#price-${event.target.name}`).innerHTML = total_price
        updateGrantTotal()
    })
}
)




