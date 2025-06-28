fetch("http://localhost:5000/products")
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("product-list");
        container.innerHTML = data.map(item => `
            <div>
                <h3>${item.name}</h3>
                <p>Price: $${item.price}</p>
                <button onclick="addToCart(${item.id})">Add to Cart</button>
            </div>
        `).join("");
    });

function addToCart(id) {
    fetch("http://localhost:5000/cart", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id })
    })
        .then(res => res.json())
        .then(data => {
            alert("Item added to cart!");
            console.log(data);
        });
}
