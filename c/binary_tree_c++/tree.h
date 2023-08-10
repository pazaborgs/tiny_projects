#include <cstddef>
#include <iostream>
#include "aluno.h"

/* struct usado para guardar a informação do objeto aluno
e os enderços da subarvore da direita e esquerda */

struct NodeType{
    Aluno aluno;
    NodeType* direita;
    NodeType* esquerda;
};

class SearchTree{
    private:
     void destroyTree(NodeType*& tree);
     void retrieveAluno(
        NodeType* tree,
        Aluno& item,
        bool& found) const;

    void insertAluno(NodeType*& tree, Aluno item);
    void deleteAluno(NodeType*& tree, int item);     
    void deleteNode(NodeType*& tree); 
    void getSuccessor(NodeType* tree, Aluno& data);
    void printTree(NodeType *tree) const;  
    void printPreOrder(NodeType* tree)  const;
    void printInOrder(NodeType* tree)   const;
    void printPostOrder(NodeType* tree) const; 
 
  //  Raiz da árvore binária de busca.
    NodeType* root;

    public:
      SearchTree() { root = NULL;  }  // Inicializa o ponteiro root como NULO
      ~SearchTree(){ destroyTree(root); } // Chama o método privado destroyTree para um ponteiro root
      bool isEmpty() const;
      bool isFull() const;
      void retrieveAluno(Aluno& item, bool& found) const{
        retrieveAluno(root, item, found); // Chama o método retrieveAluno. Retorna falso caso não exista
        }
      void insertAluno(Aluno item){ insertAluno(root, item); }  
      void deleteAluno(int item){ deleteAluno(root, item); }
      void printPreOrder()  const { printPreOrder(root); }
      void printInOrder()   const { printInOrder(root);  }
      void printPostOrder() const { printPostOrder(root);}
      
};
