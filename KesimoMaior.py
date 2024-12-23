class Solution:
    def findKthLargest(self, nums, k):

        # Encontra o k-ésimo maior elemento
        def kthLargest(nums, k):

            # Usa Mediana das Medianas para encontrar o k-ésimo elemento
            def mediana_das_medianas(arr, k):
                
                # Divide o array em grupos de 5
                def divide_em_grupos(arr):
                    return [arr[i:i+5] for i in range(0, len(arr), 5)]

                # Encontra a mediana de um grupo
                def encontrar_mediana(grupo):
                    grupo.sort()
                    return grupo[len(grupo) // 2]

                # Calcula as medianas de cada grupo
                grupos = divide_em_grupos(arr)
                medianas = [encontrar_mediana(grupo) for grupo in grupos]

                # Caso base: se houver poucas medianas, acha a mediana diretamente
                if len(medianas) <= 5:
                    medianas.sort()
                    pivo = medianas[len(medianas) // 2]
                else:
                    pivo = mediana_das_medianas(medianas, len(medianas) // 2)

                # Particiona o array com base no pivô
                menores = [x for x in arr if x > pivo]  # Maiores primeiro
                maiores = [x for x in arr if x < pivo]
                iguais = [x for x in arr if x == pivo]

                # Verifica onde está o k-ésimo maior
                if k <= len(menores):
                    return mediana_das_medianas(menores, k)
                elif k <= len(menores) + len(iguais):
                    return pivo
                else:
                    return mediana_das_medianas(maiores, k - len(menores) - len(iguais))

            return mediana_das_medianas(nums, k)

        # Chama a função para o k-ésimo maior
        return kthLargest(nums, k)
