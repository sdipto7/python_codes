import numpy as np

# print(np.__version__)
# arr = np.array([1,2,3,4,5])
#
# print(arr)
# print(type(arr))
#
# arr2 = np.array((1,2,3,4,5))
# print(arr2)
# print(type(arr2))
#
# arr3 = np.array(43)
# print(arr3)


# a = np.array([('a','b','c'),
#              ('d','e','f'),
#               ('g','h','i'),
#               ('j','k','l')])
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a[0,2])
# print(a[2,2])
# b = a.reshape(6,2)
# print(a)
# print(b)


# arr = np.arange(0,30,2)
# # arr = arr.reshape(3,5)
# # arr.resize(3,5)
# print(arr)

# a = np.linspace(0,4,9)
# a.resize(3,3)
# print(a)

# a = np.array((0,1,2,3))
# b = a.reshape(2,2)
# a.resize(2,2)
# print(a)
# print(b)


# print(np.ones((2,3),int))
# print(np.zeros((2,3)))
# print(np.eye(5))

# x = np.array(['d','i','p','u'])
# x = np.diag(x)
# print(x)
#
# y = np.array((1,2,3,4))
# y = np.diag(y)
# print(y)


# print(np.array((1,2) * 3))
# print(np.repeat([1,2],3))


# p = np.ones((2,3),int)
# q = np.vstack([p,2*p])
# print(q)
# q = np.vstack([q,2*q])
# print(q)
# r = np.hstack([p,2*p])
# print(r)
# r = np.hstack([r,2*r])
# print(r)

# a = np.ones((2,2),int)
# a = np.vstack([a,a])
# print(a)
# print("\n")
# a = np.vstack([a,a+1])
# print(a)
# print("\n")

# a = np.ones((2,2),int)
# print(np.vstack([a,2*a]))
# print(np.hstack([a,2*a]))


# x = np.array([1,2,3])
# y = np.array([4,5,6])
# print(x+y)
# print(y-x)
# print(x*y)
# print(x/y)
# print(y**2)
# print(x.dot(y))

# z = np.array([y,y**2,y**2 + 1])
# print(z)
# print(len(z))
# print(z.shape)
# print(z.T)
# print(z.T.shape)
# print(z.dtype)
# print(z)
# z = z.astype('f')
# print(z.dtype)
# print(z)


# d = np.array([-2 , -5 , 1 , 4 , 3 , 6])
# print(d.sum())
# print(d.mean())
# print(d.max())
# print(d.min())
# print(d.std())
# print(d.argmax())
# print(d.argmin())

#
# s = np.arange(0,10)**2
# # print(s[0], s[4], s[-1])
# # print(s[1:5])
# print(s)
# print(s[-4:])
# print(s[:-4])
# print(s[-5::-2])
# print(s[-8:-2:2])
# print(s[2:-2:2])


r = np.arange(25)
r.resize((5,5))
# print(r)
# print(r[2,2])
# print(r[3,3:5])
# print(r[:2,:-1])
# print(r[-1,::2])
# print(r[r>20])


# r2 = r[:3,:3]
# print(r2)
# print(r)
# r2[:]=0
# print(r2)
# print(r)
# r_copy = r.copy()
# print(r_copy)
# r_copy[:] = 10
# print(r_copy)
# print(r)


# test = np.random.randint(0,10,(2,3))
# # print(test)
# #
# # for row in test:
# #     print(row)
# #
# # # for i in range(len(test)):
# # #     print(test[i])
# #
# # for i, row in enumerate(test):
# #      print('row', i, 'is', row)
#
# # test2 = test**2
# # print(test2)
# #
# # for i, j in zip(test, test2):
# #     print(i,'+',j,'=',i+j


r = np.arange(36)
r.resize(6,6)
print(r)
r2 = r.reshape(36)[::7]
print(r2)