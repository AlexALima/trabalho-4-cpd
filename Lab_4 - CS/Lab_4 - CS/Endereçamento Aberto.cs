using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_4___CS
{
    partial class TabelaHash
    {
        static int insertHash(List<string> Tabela_Input, ref Element[] Tabela_Hash, ref int max_colisoes)
        {
            bool ocupado;
            int end, j = 1, end_aux = 0;
            string chave;
            int total_colisoes = 0;
            foreach (string x in Tabela_Input)
            {
                chave = x.Substring(0, x.IndexOf(';')); // str_aux recebe a chave
                end = computeHash(chave); // Converte a string chave para o endereço pela função Hash

                if (Tabela_Hash[end].chave != null) // Se já existir dados no endereço calculado
                {
                    ocupado = true; j = 1;
                    while (ocupado)
                    {
                        end_aux = end + j * rerandom(chave); // Calcula novo endereço
                        while (end_aux > TAMANHO_TABELA - 1) end_aux -= TAMANHO_TABELA;
                        ocupado = (Tabela_Hash[end_aux].chave != null) ? true : false;
                        j++; total_colisoes++; end = end_aux;
                    }
                    if (j > max_colisoes) max_colisoes = j;
                }
                Tabela_Hash[end].chave = chave;
                Tabela_Hash[end].dado = x.Substring(x.IndexOf(';') + 1);
            }
            return total_colisoes;
        }

        static int rerandom(string chave)
        {
            int endereco = 0, x = 1;
            foreach (int a in chave) endereco += ((a - 39) * Convert.ToInt32(Math.E * (x++)));  // Execução da função Hash: Multiplica cada caracter da chave por xe, sendo x um número inteiro de 1 ao comprimento da chave
            return endereco % TAMANHO_TABELA; // Retorna o resto da divisão do endereço calculado pelo tamanho da tabela
        }

        static void pesquisaEA(ref List<string> Tabela_Input, Element[] Tabela_Hash)
        {
            bool ocupado;
            int end, j = 1, end_aux = 0;
            readFile(ref Tabela_Input, "C:/Users/xandi/Documents/UFRGS/Classificação e Pesquisa de Dados - 2018_2/Lab_4/queries.txt");
            foreach(string x in Tabela_Input)
            {
                end = computeHash(x); // Converte a string chave para o endereço pela função Hash
                if (Tabela_Hash[end].chave == x); // Achou o dado
                else
                {
                    ocupado = true; j = 1;
                    while (ocupado && Tabela_Hash[end].chave != x)
                    {
                        end_aux = end + j * rerandom(x); // Calcula novo endereço
                        while (end_aux > TAMANHO_TABELA - 1) end_aux -= TAMANHO_TABELA;
                        ocupado = (Tabela_Hash[end_aux].chave != null) ? true : false;
                        j++;
                        end = end_aux;
                    }
                }
                if(Tabela_Hash[end].dado == null) Console.WriteLine(x + " não encontrado do dataset.");
                else Console.WriteLine(x + " é " + Tabela_Hash[end].dado);
            }
        }
    }
}
