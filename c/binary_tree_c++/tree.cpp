#include "tree.h"

//O ponteiro vai como refptr em caso em que deseja-se mudar o escopo fora da função (exclusão exemplo claro)
void SearchTree::destroyTree(NodeType*& tree){
    if (tree != NULL){
        destroyTree(tree->esquerda);
        destroyTree(tree->direita);
        delete tree;
    }
}

// Aluno é passado como referência pois é declarado fora da função, para todos os casos
void SearchTree::retrieveAluno(NodeType* tree, Aluno& aluno, bool& found) const{
    if (tree == NULL)
      found = false;
    else if (aluno.getRa() < tree ->aluno.getRa())
      retrieveAluno(tree->esquerda, aluno, found);
    else if (aluno.getRa() > tree ->aluno.getRa())
      retrieveAluno(tree->direita, aluno, found);
    else{
        aluno = tree-> aluno;
        found = true;
    }
}

void SearchTree::insertAluno(NodeType*& tree, Aluno aluno){
    if (tree == NULL)
      {
        tree = new NodeType;
        tree->direita  = NULL;
        tree->esquerda = NULL;
        tree->aluno    = aluno;
      }
  else if (aluno.getRa() < tree->aluno.getRa() )
    insertAluno(tree->esquerda, aluno);
  else
    insertAluno(tree->direita, aluno);
}
