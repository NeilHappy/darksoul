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
