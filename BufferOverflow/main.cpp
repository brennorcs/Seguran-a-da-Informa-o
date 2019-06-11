#include "ServerSocket.h"
#include "SocketException.h"
#include
  
int main ( int argc, int argv[] ){
  try{
    ServerSocket server ( 30000 );
    // insira aqui o restante do código
      
    while ( true ){
        // Aceitando a conexão solicitada
        ServerSocket new_sock;
        server.accept ( new_sock );
        
        try{
            while ( true ){
                std::string data;
                // Recebendo dados
                new_sock >> data;
                // Enviando dados
                new_sock << data;
            }
        }    
        catch ( SocketException& ) {}    
    }
  }
  catch ( SocketException& e ){
    // Tratamento de erro
    std::cout << "Exceção foi capturada:" << e.description() << " Finalizando. ";
  }
  
  return 0;
}
