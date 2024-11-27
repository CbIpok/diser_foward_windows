import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Открываем NetCDF файл с помощью xarray
ds = xr.open_dataset(r'D:\dmitrienkomy\share\set_4\dataStorage\rectangle_basis_100_10\-700_basis_11.wave.nc')

# Предположим, что ваши данные организованы как DataArray с координатами x, y, и time
# Замена 'your_variable' на имя переменной, которую вы хотите отобразить
data = ds['height']

# Получаем размеры по осям
time_steps = len(data['time'])

# Создаем фигуру и оси для графика
fig, ax = plt.subplots()

# Начальное изображение (нулевой временной шаг)
img = ax.imshow(data.isel(time=0), origin='lower', aspect='auto')
plt.colorbar(img, ax=ax)

# Функция для обновления графика на каждом шаге времени
def update(frame):
    img.set_data(data.isel(time=frame))
    ax.set_title(f'Time step: {frame}')
    return [img]

# Настройка анимации
ani = FuncAnimation(fig, update, frames=range(0,time_steps,120), interval=2)

# Показываем анимацию
plt.show()
