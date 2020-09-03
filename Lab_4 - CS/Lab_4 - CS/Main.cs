using System;
using System.IO;
using System.Collections.Generic;

namespace Lab_4___CS
{
    partial class TabelaHash
    {

        /*************** O TAMANHO DAS TABELAS SÃO NÚMEROS PRIMOS (PARA UTILIZAR O DUPLO HASHING) ***************/

        //const int TAMANHO_TABELA = 211; // Para M = 200
        const int TAMANHO_TABELA = 503; //Para M = 500
        //const int TAMANHO_TABELA = 1009; //Para M = 1000

        struct Element
        {
            public string chave, dado;
        }

        static void Main(string[] args)
        {
            Element[] Tabela_Hash = new Element[TAMANHO_TABELA];        // Cria array de Elements (inicializa a Tabela Hash)
            List<Element>[] Tabela_Hash_Encadeada = new List<Element>[TAMANHO_TABELA];        // Cria array de listas de Elements (inicializa a Tabela Hash para o endereçamento fechado)
            List<string> Tabela_Input = new List<string>();         // Tabela utilizada para ler os arquivo dataset.txt e queries.txt
            int ocupados = 0, total_colisoes = 0, max_colisoes = 0;

            readFile(ref Tabela_Input, "C:/Users/xandi/Documents/UFRGS/Classificação e Pesquisa de Dados - 2018_2/Lab_4/dataset.txt");

            total_colisoes = insertHash(Tabela_Input, ref Tabela_Hash, ref max_colisoes);

            //printHash(Tabela_Hash, ocupados, total_colisoes, max_colisoes, Tabela_Input.Count);

            pesquisaEA(ref Tabela_Input, Tabela_Hash);

            Console.ReadKey();
        }

        static void readFile(ref List<string> Tabela_Input, string fileName)
        {
            Tabela_Input.Clear(); // Limpa a lista de entrada
            using (StreamReader sr = new StreamReader(fileName)) // Leitura do arquivo
            {
                while (!sr.EndOfStream) Tabela_Input.Add(sr.ReadLine()); // Lê o arquivo e armazena todas as linhas na lista Tabela_Input
            }
        }

        static int computeHash(string chave)
        {
            int endereco = 0, x = 1;
            foreach (int a in chave) endereco += ((a - 39) * Convert.ToInt32((Math.PI * (x++))));  // Execução da função Hash: Multiplica cada caracter da chave por xπ, sendo x um número inteiro de 1 ao comprimento da chave
            return endereco % TAMANHO_TABELA; // Retorna o resto da divisão do endereço calculado pelo tamanho da tabela
        }

        static void printHash(Element[] Tabela_Hash, int ocupados, int total_colisoes, int max_colisoes, int num_elementos)
        {
            foreach (Element x in Tabela_Hash)
            {
                Console.WriteLine(x.chave + " - " + x.dado);
                if (x.chave != null) ocupados++;
            }
            Console.WriteLine("\n\nOcupação: " + ocupados + "/" + TAMANHO_TABELA + " = {0:00.00}%", Convert.ToDouble(ocupados) / TAMANHO_TABELA * 100);
            Console.WriteLine("Colisões: " + total_colisoes + " - Média de colisões: " + Convert.ToDouble(total_colisoes) / num_elementos);
            Console.WriteLine("Número máximo de colisões em uma única inserção: " + max_colisoes);
        }
    }
}
