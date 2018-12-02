import matplotlib.pyplot as plt
from matplotlib.mlab import PCA
from sklearn.manifold import TSNE
def pcCountsPCA_func(pieceRepeatsNP):
    pca = PCA(pieceRepeatsNP)
    #print('PCAs', pca.Y)
    plt.plot(pca.Y[:,10], pca.Y[:,11], 'ro') #plot first two PCAs (the ones with bigger variance)
    plt.show()
    return pca, plt

def pcCountsTSNE_func(pieceRepeatsNP):
    tsne = TSNE(n_components = 2).fit_transform(pieceRepeatsNP)
    plt.plot(tsne, 'ro', color = 'blue')
    plt.show()
    return tsne, plt
    #git comments