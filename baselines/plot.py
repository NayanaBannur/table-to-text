import os

import matplotlib.pyplot as plt

folder = './results/20220317_200809/'

train_loss = []
val_loss = []

for i in range(27):
    with open(os.path.join(folder, f'info_{i+1}.txt'), 'r') as f:
        metrics = [x.strip() for x in f.readlines()]
        d = {}
        for metric in metrics:
            k, v = metric.split('=')
            d[k.strip()] = float(v)

        train_loss.append(d['train_loss'])
        val_loss.append(d['avg_val_loss'])

plt.plot(train_loss, label='Train loss')
plt.plot(val_loss, label='Validation loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(folder, 'bart-train-val-loss-curves.png'), bbox_inches='tight', pad_inches=0.1)
plt.close()

val_mover = []

for i in range(27):
    with open(os.path.join(folder, f'info_{i+1}.txt'), 'r') as f:
        metrics = [x.strip() for x in f.readlines()]
        d = {}
        for metric in metrics:
            k, v = metric.split('=')
            d[k.strip()] = float(v)

        val_mover.append(d['val_mover'])

plt.plot(val_mover)
plt.xlabel('Epoch')
plt.ylabel('MoverScore')
plt.tight_layout()
plt.savefig(os.path.join(folder, 'bart-val-mover.png'), bbox_inches='tight', pad_inches=0.1)
plt.close()

folder = './results/20220318_060908/'

train_loss = []
val_loss = []

for i in range(27):
    with open(os.path.join(folder, f'info_{i+1}.txt'), 'r') as f:
        metrics = [x.strip() for x in f.readlines()]
        d = {}
        for metric in metrics:
            k, v = metric.split('=')
            d[k.strip()] = float(v)

        train_loss.append(d['train_loss'])
        val_loss.append(d['avg_val_loss'])

plt.plot(train_loss, label='Train loss')
plt.plot(val_loss, label='Validation loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(folder, 't5-train-val-loss-curves.png'), bbox_inches='tight', pad_inches=0.1)
plt.close()

val_mover = []

for i in range(27):
    with open(os.path.join(folder, f'info_{i+1}.txt'), 'r') as f:
        metrics = [x.strip() for x in f.readlines()]
        d = {}
        for metric in metrics:
            k, v = metric.split('=')
            d[k.strip()] = float(v)

        val_mover.append(d['val_mover'])

plt.plot(val_mover)
plt.xlabel('Epoch')
plt.ylabel('MoverScore')
plt.tight_layout()
plt.savefig(os.path.join(folder, 't5-val-mover.png'), bbox_inches='tight', pad_inches=0.1)
plt.close()
