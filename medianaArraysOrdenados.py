class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Junta os dois arrays em um único
        mesclar = nums1 + nums2

        # Função algoritmo Mediana das Medianas
        def mediana_das_medianas(arr, k):
            # Divide o array em grupos de 5
            def dividir_em_grupos(arr):
                return [arr[i:i+5] for i in range(0, len(arr), 5)]

            # Encontra a mediana de um grupo
            def encontrar_mediana(grupo):
                grupo.sort()
                return grupo[len(grupo) // 2]

            # Calcula as medianas de cada grupo
            grupos = dividir_em_grupos(arr)
            medianas = [encontrar_mediana(grupo) for grupo in grupos]

            # Caso base: se houver apenas uma mediana, retorna ela
            if len(medianas) <= 5:
                medianas.sort()
                pivo = medianas[len(medianas) // 2]
            else:
                pivo = mediana_das_medianas(medianas, len(medianas) // 2)

            # Particiona o array em relação ao pivô
            menores = [x for x in arr if x < pivo]
            maiores = [x for x in arr if x > pivo]
            pivos = [x for x in arr if x == pivo]

            # Determina a posição do k-ésimo elemento
            if k < len(menores):
                return mediana_das_medianas(menores, k)
            elif k < len(menores) + len(pivos):
                return pivo
            else:
                return mediana_das_medianas(maiores, k - len(menores) - len(pivos))

        n = len(mesclar)

        # Calcula a mediana para arrays com comprimento ímpar e par
        if n % 2 == 1:
            return mediana_das_medianas(mesclar, n // 2)
        else:
            return (mediana_das_medianas(mesclar, n // 2 - 1) + mediana_das_medianas(mesclar, n // 2)) / 2.0
