const objetoCliente = {
    id: 5,
    nome: "arisberto",
    idade: 26,
    cpf: "999.888.777-22"

}

console.log(`Nome: ${objetoCliente[`nome`]}`)
console.log(`idade: ${objetoCliente[`idade`]}`)
console.log(`cpf: ${objetoCliente[`cpf`]}`)

const chave = ["nome", "idade", "cpf"]

chave.forEach((chave) => {
        console.log(`chave: ${chave} valor: ${objetoCliente[chave]}`)});
