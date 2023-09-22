package singlylinkedlists

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"reflect"
	"testing"
)

func TestSinglyLinkedList_GetFirstValue(t *testing.T) {
	list := New[string]()
	_, err := list.GetFirstValue()
	assert.NotNil(t, err)
	list.Add("abc")

	value, err := list.GetFirstValue()
	assert.Nil(t, err)
	assert.Equal(t, "abc", value)

	list.Add("def")
	value, err = list.GetFirstValue()
	assert.Nil(t, err)
	assert.Equal(t, "abc", value)

	list.InsertAt(0, "111")
	value, err = list.GetFirstValue()
	assert.Nil(t, err)
	assert.Equal(t, "111", value)

}

func TestSinglyLinkedList_GetLastValue(t *testing.T) {
	list := New[string]()

	_, err := list.GetLastValue()
	assert.NotNil(t, err)

	list.Add("abc")
	value, err := list.GetLastValue()
	assert.Nil(t, err)
	assert.Equal(t, "abc", value)

	list.Add("def")
	value, err = list.GetLastValue()
	assert.Nil(t, err)
	assert.Equal(t, "def", value)

	list.InsertAt(2, "222")
	value, err = list.GetLastValue()
	assert.Nil(t, err)
	assert.Equal(t, "222", value)

}

func TestSinglyLinkedList_GetValues(t *testing.T) {
	list := New[string]()
	assert.True(t, reflect.DeepEqual(list.GetValues(), []string{}))

	list.Add("a", "b", "c")
	assert.True(t, reflect.DeepEqual(list.GetValues(), []string{"a", "b", "c"}))

	list.InsertAt(1, "d")
	assert.True(t, reflect.DeepEqual(list.GetValues(), []string{"a", "d", "b", "c"}))

}

func TestSinglyLinkedList_IsEmpty(t *testing.T) {
	list := New[string]()
	assert.Equal(t, list.IsEmpty(), true)

	list.Add("abc")
	assert.Equal(t, list.IsEmpty(), false)

	res, err := list.RemoveAt(1)
	fmt.Println(res)
	assert.True(t, reflect.DeepEqual(res, ""))
	assert.NotNil(t, err)
	assert.Equal(t, list.IsEmpty(), false)

	list.RemoveAt(0)
	assert.Equal(t, list.IsEmpty(), true)

}

func TestSinglyLinkedList_Size(t *testing.T) {
	list := New[string]()
	list.Add("abc")
	assert.Equal(t, list.Size(), 1)
	list.Add("abc")
	assert.Equal(t, list.Size(), 2)
	list.Add("abc")
	assert.Equal(t, list.Size(), 3)
	list.Add("abc")
	assert.Equal(t, list.Size(), 4)
	list.RemoveAt(0)
	assert.Equal(t, list.Size(), 3)
	list.RemoveAt(0)
	assert.Equal(t, list.Size(), 2)

}

func TestSinglyLinkedList_GetIndexOf(t *testing.T) {
	list := New[string]()
	assert.Equal(t, list.GetIndexOf("abc"), -1)
	list.Add("abc")
	assert.Equal(t, list.GetIndexOf("abc"), 0)
	list.Add("def")
	assert.Equal(t, list.GetIndexOf("def"), 1)
	list.Add("def")
	assert.Equal(t, list.GetIndexOf("def"), 1)

}

func TestSinglyLinkedList_InsertAt(t *testing.T) {
	list := New[string]()
	err := list.InsertAt(0, "abc")
	assert.Nil(t, err)

	err = list.InsertAt(3, "abc")
	assert.NotNil(t, err)

}

func TestSinglyLinkedList_RemoveAt(t *testing.T) {
	list := New[string]()
	_, err := list.RemoveAt(0)
	assert.NotNil(t, err)

	list.Add("abc")
	value, err := list.RemoveAt(0)
	assert.Nil(t, err)
	assert.True(t, reflect.DeepEqual(value, "abc"))

}

func TestSinglyLinkedList_Clear(t *testing.T) {
	list := New[string]()
	list.Add("abc")
	list.Clear()
	assert.True(t, reflect.DeepEqual(list.GetValues(), []string{}))
	assert.Equal(t, list.Size(), 0)
	assert.Equal(t, list.IsEmpty(), true)

	list.Add("abc")
	list.Clear()
	assert.True(t, reflect.DeepEqual(list.GetValues(), []string{}))
	assert.Equal(t, list.Size(), 0)
	assert.Equal(t, list.IsEmpty(), true)

}
