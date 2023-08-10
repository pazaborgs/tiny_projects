export default class Candidato
{
    constructor(nome, legenda, numero, img, num_votos)
    {
        this.nome = nome;
        this.legenda = legenda;
        this.numero = numero;
        this.img = img;
        this.num_votos = num_votos;
    }

    get nomeCandidato()
    {
        return this.nome
    }


}